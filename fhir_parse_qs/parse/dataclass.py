from collections import namedtuple
from pendulum import parse
from fhir_parse_qs.mappings import search_parameters

__all__=['Search']

FHIRSearchPair = namedtuple("FHIRSearchPair", 'modifier prefix parameter value type_ chain')

class Search:
    """
    A FHIR search query:

    resource is string of the FHIR resource
    query_string is string of the query string
    mapping is dict of {search_param: type} that overrides default (optional)

    """

    def __init__(self, resource, query_string, mapping=None):

        self.allowed_basic_mods = ['exact', 'missing', 'exists', 'contains', 'text', 'in', 'above', 'below', 'not-in']
        self.allowed_prefixes = ['eq', 'ne', 'gt', 'lt', 'ge', 'le', 'sa', 'eb', 'ap']
        self.resource = resource
        self.search_parameters = search_parameters
        self.qs = query_string
        self.search_types = {
                'number': float,
                'string': str,
                'reference': str,
                'token': str,
                'date': parse,
                'composite': str,
                'quantity': str,
                'uri': str
                }

        self.errors = []

        if not mapping:
            try:
                self.search_mapping = self.search_parameters[resource]
                self.search_mapping.update(self.search_parameters['ctrl_parameters']) #update with common
                self.search_mapping.update(self.search_parameters['common_parameters']) #update with common
            except:
                raise ValueError('{} is not a supported endpoint; Please provide mapping'.format(resource))
        else:
            self.search_mapping = mapping

        self.parsed_qs = self.parse_qs(query_string)

    def __getitem__(self, key):
        """
        Retrieves FHIRSearch by parameter or index
        """

        if self.parsed_qs is None: raise TypeError('Not indexable')
        found = []
        if isinstance(key, str):
            for item in self.parsed_qs:
                if item.parameter == key: found.append(item)
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
        return '<FHIR search on {}, {} parameters>'.format(self.resource, len(self.parsed_qs))

    def __len__(self):
        return len(self.parsed_qs)

    def __iter__(self):
        return iter(self.parsed_qs)

    @staticmethod
    def naive_parse_qs(qs):
        from urllib.parse import parse_qsl
        return parse_qsl(qs)

    def parse_qs(self, qs):
        naive_pairs = self.naive_parse_qs(qs)
        pairs = []
        for param, value in naive_pairs:

            #Get modifier
            par, mod = self.getModifier(param)

            # Chain parsing
            par, chains = self.getChain(par)

            # If parameter not supported, ignore and add to errors
            try:
                type_ = self.search_mapping[par]
            except:
                self.errors.append('Parameter <{}> not found in mapping; Ignoring'.format(par))
                continue

            # Does type allow chaining
            if chains and not self.allowsChain(type_):
                self.errors.append('Parameter <{}> does not allow chaining; Ignoring'.format(par))
                continue

            if mod:
                if not self.validModifier(mod, type_):
                    raise TypeError('The {} search parameter cannot have modifier {}'.format(par, mod))

            #Prefix
            pre, v = self.getPrefix(value, type_)

            #Get validated value
            value = self.getValidType(type_, v)
            if value is False: raise ValueError('Cannot cast {} to type {}'.format(v, type_))

            pairs.append(FHIRSearchPair(modifier=mod, prefix=pre, value=value, parameter=par, type_=type_, chain=chains))

        return pairs

    def getValidType(self, type_, value):
        """
        Returns parsed value if correct type or False
        """
        try:
            return self.search_types[type_](value)
        except:
            return False

    def getPrefix(self, value, type_):
        """
        Returns (prefix, base_value) or (None, base_value)

        Only number, date, and quantity allow prefixes
        """
        if type_ in ('number','date', 'quantity'):
            for pf in self.allowed_prefixes:
                if value.startswith(pf):
                    return value[:2], value[2:]
        return None, value

    def validModifier(self, modifier, type_):
        """
        All types allow certain modifiers, consequently need type of parameter, too, for further validation

        Returns true if type allows modifier, else false
        """
        # TODO Add reference 'type' modifier logic
        if type_ == 'reference': return True # e.g., :Patient.name, :Observation.id
        if modifier in ('missing', 'exists'): return True
        if modifier in ('exact', 'contains') and type_ == 'string': return True
        if modifier in ('text', 'in', 'below', 'above', 'not-in') and type_ == 'token': return True
        if modifier in ('below', 'above') and type_ == 'uri': return True
        return False

    def getModifier(self, parameter):
        """
        Splits on ':'

        Returns (base_parameter, modifier) or (parameter, None)

        """
        base, *mod = parameter.split(':')
        if mod:
            return base, mod[0] #Should only be 1 (?)
        return base, None

    def allowsChain(self, type_):
        """
        Can only chain references
        """
        return True if type_ == 'reference' else False

    def getChain(self, parameter):
        """
        Parse chains - split on '.'

        Returns (base_parameter, [chain(s)]) or (parameter, None)
        """
        base, *chain = parameter.split('.')
        return base, chain or None

    @property
    def modifier(self):
        """
        Returns all modifiers
        """
        return [x.modifier for x in self.parsed_qs if x.modifier is not None]

    @property
    def prefix(self):
        """
        Returns all prefixes
        """
        return [x.prefix for x in self.parsed_qs if x.prefix is not None]

    @property
    def value(self):
        """
        Returns all values
        """
        return [x.value for x in self.parsed_qs]

    @property
    def parameter(self):
        """
        Returns all parameters
        """
        return [x.parameter for x in self.parsed_qs]

    @property
    def endpoint(self):
        """
        Returns the search resource
        """
        return self.resource

    @property
    def unparsed(self):
        """
        Raw query string
        """
        return self.qs

    @property
    def parsed(self):
        """
        Returns list of search queries
        """
        return self.parsed_qs

    @property
    def error(self):
        """
        Non-critical errors during parsing
        """
        return self.errors
