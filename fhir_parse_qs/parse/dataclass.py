from collections import namedtuple
from pendulum import parse
from fhir_parse_qs.mappings import search_references, search_types

__all__ = ["Search"]

FHIRSearchPair = namedtuple(
    "FHIRSearchPair", "modifier prefix parameter value type_ chain"
)
FHIRChain = namedtuple("FHIRChain", "endpoint target ttype")


class Search:
    """A FHIR search query

    :Example:

    >>> import fhir_parse_qs
    >>> query = fhir_parse_qs.Search('Patient', 'name=peter')
    >>> query.endpoint
    'Patient'

    .. note:: This class uses namedtuples
        - FHIRSearchPair: modifier, prefix, parameter, value, type_, chain
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
        "date": parse,
        "composite": str,
        "quantity": float,
        "uri": str,
    }
    supported = [k for k in search_types.keys() if k not in ("control", "common")]

    def __init__(self, resource, query_string, mapping=None):
        """
        Instantiates class with target endpoint and query string

        :param resource: target FHIR resource
        :type resource: str
        :param query_string: query string
        :type query_string: str
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
        Retrieves FHIRSearchPain by parameter or index

        :param key: key
        :type key: str or int
        :rtype: list(FHIRSearchPair) or list(FHIRSearchPair)

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

        from urllib.parse import parse_qsl

        return parse_qsl(qs)

    def parse_qs(self, qs):
        """Parse the query string

        :param qs: query string
        :type qs: str
        :return: parsed query string
        :rtype: list(FHIRSearchPair)
        """

        naive_pairs = self.naive_parse_qs(qs)
        pairs = []
        for param, value in naive_pairs:

            # 1) Get any modifiers on parameter
            # 2) Parse any chains on parameter
            # 3) Parse any prefixes on value
            # 4) Cast the value to type

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

            # Prefix
            pre, v = self.getPrefix(value, type_)

            # Cast the value
            value = self.getValidType(type_, v)
            if value is False:
                raise ValueError("Cannot cast '{}' to type '{}'".format(v, type_))

            pairs.append(
                FHIRSearchPair(
                    modifier=mod,
                    prefix=pre,
                    value=value,
                    parameter=par,
                    type_=type_,
                    chain=chain_tree,
                )
            )

        return pairs

    def getValidType(self, type_, value):
        """
        Returns parsed value in correct type or False

        :param type_: parameter type
        :type type_: str
        :param value: parameter value
        :type value: str
        :return: cast value or False if failed
        :rtype: variable


        .. TODO:: Full quantity support [parameter]=[prefix][number]|[system]|[code]
        .. TODO:: Full token support [parameter]=[system]|[code] (system optional)
        """
        try:
            if type_ == "quantity":
                value = value.split("|")[0]  # Ignore system and code
            if type_ == "token":
                value = value.split("|")[-1]  # Ignore system
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

    def getModifier(self, parameter):
        """
        Split on ':' to get any modifiers

        :param parameter: target string
        :type parameter: str
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
