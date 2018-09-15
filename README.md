A library to parse FHIR query strings.

- Validates type and returns correct object
- Built-in search parameters from FHIR standard
- Parses modifiers and prefixes

Generally only have included Resources with maturity greater than 2. Some exceptions.

#### Usage

    from fhir_parse_qs import Search
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
    search[0].paramater --> 'name'
    search[0].type_ --> 'string'

    # act like dict with parameter as key (list if non-unique parameter)
    search['name'] --> FHIRSearch(...)

    # can iterate over the paramater/value pairs
    for x in search:
         print(x) --> FHIRSearch(...)

    # if does not recognize parameter, ignores it and adds to error
    search = Search('Patient', 'random=test')
    search.error --> [...]
