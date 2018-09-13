A library to parse FHIR query strings.

- Validates type and returns correct object
- Parses modifiers and prefixes

#### Usage

    from fhir_parse_qs import Search
    search = Search('Patient', 'name=bob')

    # what endpoint
    print(search.resource) --> 'Patient'

    # each parameter/value pair gets parsed into a namedtuple
    search.parsed[0] --> FHIRSearch

    # all the namedtuples
    search.parsed --> [FHIRSearch]

    search.parsed[0].modifier --> None
    search.parsed[0].prefix --> None
    search.parsed[0].value --> 'bob'
    search.parsed[0].paramater --> 'name'

    # can iterate over the paramater/value pairs
    for x in search:
        print(x) --> FHIRSearch
