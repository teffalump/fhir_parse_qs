from collections import namedtuple
from urllib.parse import parse_qsl
from pendulum import parse as parse_dt
from fhir_parse_qs.mappings import search_references, search_types

__all__ = ["Search"]

FHIRSearchPair = namedtuple(
    "FHIRSearchPair", "modifier prefix parameter value type_ chain system code"
)
FHIRChain = namedtuple("FHIRChain", "endpoint target ttype")


class Search:
    """A FHIR search query

    :Example:

    >>> from fhir_parse_qs import Search
    >>> query = Search('Patient', 'name=peter')
    >>> query.endpoint
    'Patient'

    .. note:: This class uses namedtuples
        - FHIRSearchPair: modifier, prefix, parameter, value, type_, chain, system, code
        - FHIRChain: endpoint, target, ttype
    """

    # Static elements
    allowed_basic_mods = [
        "exact",
        "missing",
        "exists",
        "contains",
        "text",
        "in",
        "above",
        "below",
        "not-in",
    ]
    allowed_prefixes = ["eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap"]
    all_types = search_types
    all_references = search_references
    search_cast = {
        "number": float,
        "string": str,
        "reference": str,
        "token": str,
        "date": parse_dt,
        "composite": str,
        "quantity": float,
        "uri": str,
    }
    supported = [k for k in search_types.keys() if k not in ("control", "common")]

    def __init__(self, resource, query_string, mapping=None):
        """
        Instantiates class with target endpoint and query string

        :param str resource: target FHIR resource
        :param str query_string: query string
        :param mapping: mapping than overrides default (optional)
        :type mapping: dict(str, str)
        """

        self.resource = resource
        self.qs = query_string
        self.errors = []
        if not mapping:
            try:
                self.search_mapping = self.all_types[resource]
                self.search_mapping.update(self.all_types["control"])
                self.search_mapping.update(self.all_types["common"])
            except:
                raise ValueError(
                    "{} is not a supported endpoint; Please provide mapping".format(
                        resource
                    )
                )
        else:
            self.search_mapping = mapping

        self.parsed_qs = self.parse_qs(query_string)

    def __getitem__(self, key):
        """
        Retrieves FHIRSearchPair by parameter or index

        :param key: key
        :type key: str or int
        :rtype: list(FHIRSearchPair) or FHIRSearchPair

        """

        if self.parsed_qs is None:
            raise TypeError("Not indexable")
        found = []
        if isinstance(key, str):
            for item in self.parsed_qs:
                if item.parameter == key:
                    found.append(item)
        else:
            try:
                found.append(self.parsed_qs[key])
            except:
                pass

        if not found:
            raise KeyError(key)
        if len(found) == 1:
            return found[0]
        else:
            return found

    def __repr__(self):
        return "<FHIR search on {}, {} parameter(s), {} errors>".format(
            self.resource, len(self.parsed_qs), len(self.errors)
        )

    def __len__(self):
        return len(self.parsed_qs)

    def __iter__(self):
        return iter(self.parsed_qs)

    @staticmethod
    def naive_parse_qs(qs):
        """Wrapper for urllib.parse.parse_qsl"""

        return parse_qsl(qs)

    def parse_qs(self, qs):
        """Parse the query string

        :param str qs: query string
        :return: parsed query string
        :rtype: list(FHIRSearchPair)
        """

        naive_pairs = self.naive_parse_qs(qs)
        pairs = []
        for param, value in naive_pairs:

            # 1) Get any modifiers on parameter
            # 2) Parse any chains on parameter
            # 3) Parse the value string according to parameter type
            # 4) Cast the value according to parameter type

            # Get modifier
            par, mod = self.getModifier(param)

            # Chain parsing with modifier as resource
            # e.g., :Patient.name
            if mod and self.getChain(mod)[1]:
                target_ep, chains = self.getChain(mod)
                mod = None  # not a true modifier
            else:
                par, chains = self.getChain(par)
                target_ep = None

            # If parameter not supported, ignore and add to errors
            try:
                type_ = self.search_mapping[par]
            except:
                self.errors.append(
                    "<parameter> '{}' not found in mapping; Ignoring".format(par)
                )
                continue

            # Does type allow chaining
            if chains and not self.allowsChain(type_):
                self.errors.append(
                    "<parameter> '{}' does not allow chaining; Ignoring".format(par)
                )
                continue

            # Chains
            if chains:
                # If there is specified endpoint
                if target_ep:
                    if target_ep in self.all_references[self.resource][par]:
                        chain_tree = [
                            x
                            for x in self.getValidChains(self.resource, [par] + chains)
                            if x[1].endpoint == target_ep
                        ]
                    else:
                        self.errors.append(
                            "'{}' is not valid reference endpoint for <parameter> '{}'".format(
                                target_ep, par
                            )
                        )
                        continue
                else:
                    chain_tree = self.getValidChains(self.resource, [par] + chains)
            else:
                chain_tree = None

            # Chain overrules the original type and parameter
            if chain_tree:
                type_ = chain_tree[0][-1].ttype
                par = chain_tree[0][-1].target

            if mod:
                if not self.validModifier(mod, type_):
                    raise TypeError(
                        "<parameter> '{}' of <type> '{}' cannot have modifier '{}'".format(
                            par, type_, mod
                        )
                    )

            # Parse value string and cast it according to type
            if type_ == "quantity":
                value_dict = self.parse_quantity(value)
            elif type_ == "token":
                value_dict = self.parse_token(value)
            elif type_ == "uri":
                value_dict = self.parse_uri(value)
            elif type_ == "string":
                value_dict = self.parse_string(value)
            elif type_ == "date":
                value_dict = self.parse_date(value)
            elif type_ == "number":
                value_dict = self.parse_number(value)
            elif type_ == "reference":
                value_dict = self.parse_reference(value)
            elif type_ == "composite":
                value_dict = self.parse_composite(value)
            elif type_ == "special":
                value_dict = self.parse_special(value)
            else:
                raise TypeError("Unknown type {}".format(type_))

            pairs.append(
                FHIRSearchPair(
                    modifier=mod,
                    prefix=value_dict["prefix"],
                    value=value_dict["value"],
                    parameter=par,
                    type_=type_,
                    chain=chain_tree,
                    system=value_dict["system"],
                    code=value_dict["code"],
                )
            )

        return pairs

    def cast_value(self, parameter_type, parameter_value):
        """Cast value according to parameter type

        :param str parameter_type: parameter type
        :param str parameter_value: parameter value
        :return: cast value
        :rtype: variable
        :raises ValueError: If error while casting
        """
        value = self.getValidType(parameter_type, parameter_value)
        if value is False:
            raise ValueError(
                "Cannot cast '{}' to type '{}'".format(parameter_value, parameter_type)
            )
        return value

    def getValidType(self, type_, value):
        """
        Returns parsed value in correct type or False

        :param str type_: parameter type
        :param str value: parameter value
        :return: cast value or False if failed
        :rtype: variable

        """
        try:
            return self.search_cast[type_](value)
        except:
            return False

    def getPrefix(self, value, type_):
        """
        Returns valid prefixes

        :param value: unparsed string
        :type value: str
        :param type_: parameter type
        :type type_: str
        :return: (prefix, base_value) or (None, base_value)
        :rtype: tuple(str, str) or tuple(None, str)

        .. NOTE:: Only number, date, and quantity allow prefixes
        """

        if type_ in ("number", "date", "quantity"):
            for pf in self.allowed_prefixes:
                if value.startswith(pf):
                    return value[: len(pf)], value[len(pf) :]
        return None, value

    def validModifier(self, modifier, type_):
        """
        Validate modifier

        :param modifier: modifier to check
        :type modifier: str
        :param type_: parameter type
        :type type_: str
        :return: True or False
        :rtype: True or False

        .. TODO:: Add reference 'type' modifier logic
        """
        if type_ == "reference":
            return True  # e.g., :Patient.name, :Observation.id
        if modifier in ("missing", "exists"):
            return True
        if modifier in ("exact", "contains") and type_ == "string":
            return True
        if modifier in ("text", "in", "below", "above", "not-in") and type_ == "token":
            return True
        if modifier in ("below", "above") and type_ == "uri":
            return True
        return False

    def get_composite_sequence(self, value):
        """
        Split on '$' to obtain composite search parameters.

        :param str value:
            Target string
        :return:
            List of strings of composite search
        :rtype:
            list

        """
        return value.split("$")

    def get_system_and_code(self, value, quantity=True):
        """
        Extract the system and code values. Both `Token` and `Quantity` types use these extensively (but differently).

        Quantity = [prefix][number]|[system]|[code]
        Token = [system]|[code] --- code is value, system can be value, too (strange)

        :param str value:
            Query string
        :param bool quantity:
            If Quantity type or not. Default True.
        :return:
            Parsed value
        :rtype:
            dict
        """

        if quantity == True:
            number, *units = value.split("|")
            if units:  # Has postfix
                return {"number": number, "system": units[0], "code": units[1]}
            else:
                return {"number": number, "system": "", "code": ""}
        else:
            units = value.split("|")
            if len(units) == 1:
                return {"code": units[0], "system": ""}
            else:
                return {"system": units[0], "code": units[1]}

    def parse_special(self, full_string):
        """Parse a special-type value string.

        Treated as a simple string.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict

        ::note: Composite parameters do not have modifiers
        """

        # Parse value and prefix
        prefix, value = self.getPrefix(full_string, "special")

        # Cast value
        cast_value = self.cast_value("special", value)

        return {
            "value": cast_value,
            "prefix": prefix,
            "system": None,
            "code": None,
        }

    def parse_composite(self, full_string):
        # TODO Do not know how to parse this as not entirely on standard
        #       parameter$value ?? and parameter$value,value --- very confused
        """Parse a composite-type value string.

        The standard is generally hard to interpret but seems to be:

            [parameter] = [other_defined_parameter]$[value]$[value], etc

        Given difficulty understanding standard, parse as simple string

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict

        ::note: Composite parameters do not have modifiers
        """

        # Parse value and prefix
        prefix, value = self.getPrefix(full_string, "composite")

        # Cast value
        cast_value = self.cast_value("composite", value)

        return {
            "value": cast_value,
            "prefix": prefix,
            "system": None,
            "code": None,
        }

    def parse_quantity(self, full_string):
        """Parse a quantity-type value string.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        # Parse postfix (system and code)
        expr_dict = self.get_system_and_code(full_string, quantity=True)

        # Parse value and prefix
        prefix, value = self.getPrefix(expr_dict["number"], "quantity")

        # Cast value
        cast_value = self.cast_value("quantity", value)

        return {
            "value": cast_value,
            "prefix": prefix,
            "system": expr_dict["system"] or None,
            "code": expr_dict["code"] or None,
        }

    def parse_token(self, full_string):
        """ Parse a token-type value string.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        # Parse postfix (system and code)
        expr_dict = self.get_system_and_code(full_string, quantity=False)

        # Parse value and prefix
        prefix, value = self.getPrefix(expr_dict["code"], "token")

        # Cast value
        cast_value = self.cast_value("token", value)

        return {
            "value": cast_value,
            "prefix": prefix,
            "system": expr_dict["system"] or None,
            "code": None,
        }

    def parse_reference(self, full_string):
        """ Parse a reference-type value string.

        Per standard:

            [parameter]=[id] the logical [id] of a resource using a local reference (i.e. a relative reference)
            [parameter]=[type]/[id] the logical [id] of a resource of a specified type using a local reference (i.e. a relative reference), for when the reference can point to different types of resources (e.g. Observation.subject)
            [parameter]=[url] where the [url] is an absolute URL - a reference to a resource by its absolute location, or by it's canonical URL

        As such, no need for complex parsing.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """
        prefix, value = self.getPrefix(full_string, "reference")

        # Cast value
        cast_value = self.cast_value("reference", value)

        return {"value": cast_value, "prefix": prefix, "system": None, "code": None}

    def parse_uri(self, full_string):
        """ Parse a uri-type value string.

        Per standard, there is no special parsing.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        prefix, value = self.getPrefix(full_string, "uri")

        # Cast value
        cast_value = self.cast_value("uri", value)

        return {"value": cast_value, "prefix": prefix, "system": None, "code": None}

    def parse_string(self, full_string):
        """ Parse a string-type value string.

        Per standard, there is no special parsing.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        prefix, value = self.getPrefix(full_string, "string")

        # Cast value
        cast_value = self.cast_value("string", value)

        return {"value": cast_value, "prefix": prefix, "system": None, "code": None}

    def parse_number(self, full_string):
        """ Parse a number-type value string.

        Per standard, there is no special parsing.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        prefix, value = self.getPrefix(full_string, "number")

        # Cast value
        cast_value = self.cast_value("number", value)

        return {"value": cast_value, "prefix": prefix, "system": None, "code": None}

    def parse_date(self, full_string):
        """ Parse a date-type value string.

        Per standard, there is no special parsing.

        :param str full_string: Unadulterated value string
        :return:
            Parsed value string into dictionary
        :return:
            dict
        """

        prefix, value = self.getPrefix(full_string, "date")

        # Cast value
        cast_value = self.cast_value("date", value)

        return {"value": cast_value, "prefix": prefix, "system": None, "code": None}

    def getModifier(self, parameter):
        """
        Split on ':' to get any modifiers

        :param str parameter: target string
        :return: (base_parameter, modifier) or (parameter, None)
        :rtype: tuple(str, str) or tuple(str, None)
        """

        base, *mod = parameter.split(":")
        if mod:
            return base, mod[0]  # Should only be 1 (?)
        return base, None

    def getValidChains(self, resource, chains, saved=[]):
        """
        Wrapper for getChainTree, returning non-empty paths

        :param resource: endpoint
        :type resource: str
        :param chains: chains to use
        :type chains: list(str)
        :return: non-empty, valid paths or exception (if no paths)
        :rtype: list(list(FHIRChain)) or TypeError
        """

        temp = [x for x in self.getChainTree(saved, resource, chains) if x]
        if not temp:
            raise TypeError("No valid chains")
        return temp

    def allowsChain(self, type_):
        """
        Can only chain references

        :param type_: parameter type
        :type type_: str
        :return: True or False
        :rtype: True or False
        """
        return True if type_ == "reference" else False

    def getChain(self, parameter):
        """
        Parse chains by splitting on '.'

        :param parameter: target parameter
        :type parameter: str
        :return: (base_parameter, [chain(s)]) or (parameter, None)
        :rtype: tuple(str, list(str)) or tuple(str, None)
        """
        base, *chain = parameter.split(".")
        return base, chain or None

    def getChainTree(self, saved=[], resource=None, chains=[]):
        """
        Recursively generates paths given chains

        :param saved: previously saved path
        :type saved: list(FHIRChain)
        :param resource: current endpoint
        :type resource: str
        :param chains: remaining chains
        :type chains: list(str)
        :return: resource paths
        :rtype: list(list(FHIRChain))
        """

        curr, chains = chains[0], chains[1:]
        if not chains:
            try:
                d = self.all_types[resource][curr]
                if d == "reference":
                    return []  # invalid if ends on reference
                else:
                    return saved + [FHIRChain(endpoint=resource, target=curr, ttype=d)]
            except:
                return []  # invalid if not valid parameter
        else:
            try:
                rs = self.all_references[resource][curr]
            except:
                return []  # invalid if not valid reference
            return [
                self.getChainTree(
                    saved
                    + [FHIRChain(endpoint=resource, target=curr, ttype="reference")],
                    r,
                    chains,
                )
                for r in rs
            ]

    @property
    def modifier(self):
        """
        Returns all modifiers

        :return: modifiers in parameters
        :rtype: list(str)
        """

        return [x.modifier for x in self.parsed_qs if x.modifier is not None]

    @property
    def prefix(self):
        """
        Returns all prefixes

        :return: prefixes in values
        :rtype: list(str)
        """

        return [x.prefix for x in self.parsed_qs if x.prefix is not None]

    @property
    def value(self):
        """
        Returns all values

        :return: values in query string
        :rtype: list(str)
        """

        return [x.value for x in self.parsed_qs]

    @property
    def parameter(self):
        """
        Returns all parameters

        :return: parameters in query string
        :rtype: list(str)
        """

        return [x.parameter for x in self.parsed_qs]

    @property
    def endpoint(self):
        """
        Returns the endpoint

        :return: endpoint
        :rtype: str
        """

        return self.resource

    @property
    def unparsed(self):
        """
        Returns the original, raw query string

        :return: raw query string
        :rtype: str
        """

        return self.qs

    @property
    def parsed(self):
        """
        Returns the list of search queries

        :return: search queries
        :rtype: list(FHIRSearchPair)
        """

        return self.parsed_qs

    @property
    def control(self):
        """
        Returns control parameters

        :return: control parameters in query string
        :rtype: list(str)
        """

        return [x for x in self.parsed_qs if x.parameter in self.all_types["control"]]

    @property
    def error(self):
        """
        Returns non-critical errors during parsing

        :return: errors during parsing
        :rtype: list(str)
        """

        return self.errors
