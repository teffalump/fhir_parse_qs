A library to parse FHIR query strings.

- Validates type and returns correct object
- Built-in search parameters from FHIR standard
- Supports modifiers, prefixes, and chains

Generally only have included relevant Resources with maturity greater than 2. Some exceptions.

#### Usage

    from fhir_parse_qs import Search

    # supported endpoints
    Search.supported --> [...]

    # simple use
    search = Search('Patient', 'name=bob') # Search(<endpoint>, <query_string>)

    # endpoint
    search.endpoint --> 'Patient'

    # all the namedtuples
    search.parsed --> [FHIRSearch(...)]

    # index as key; each parameter/value pair gets parsed into a namedtuple
    search[0] --> FHIRSearch(...)
    search[0].modifier --> None
    search[0].prefix --> None
    search[0].value --> 'bob'
    search[0].parameter --> 'name'
    search[0].type_ --> 'string'
    search[0].chain --> None

    # act like dict with parameter as key
    search['name'] --> FHIRSearch(...) #list if non-unique parameter

    # can iterate over the parameter/value pairs
    for x in search:
         print(x) --> FHIRSearch(...)

    # unrecognized parameter, ignore and log it
    search = Search('Patient', 'random=test')
    search.error --> [...]

    # chains - namedtuple with endpoint, target_parameter, target_type
    search = Search('Observation', 'patient.name=peter')
    search[0].parameter --> 'name' # last parameter in chain
    search[0].value --> 'peter'
    search[0].chain --> [FHIRChain(...), FHIRChain(...)]
    search[0].chain[0].endpoint = 'Observation'
    search[0].chain[0].target = 'patient'
    search[0].chain[0].ttype = 'reference'
    search[0].chain[1].endpoint = 'Patient'
    search[0].chain[1].target = 'name'
    search[0].chain[1].ttype = 'string'

    # return control parameters (eg, _sort, _count, etc)
    search.control --> [...]
