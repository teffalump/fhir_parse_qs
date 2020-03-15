# fhir_parse_qs

[![Build Status](https://travis-ci.com/teffalump/fhir_parse_qs.svg?branch=master)](https://travis-ci.com/teffalump/fhir_parse_qs)
[![PyPI version](https://badge.fury.io/py/fhir-parse-qs.svg)](https://badge.fury.io/py/fhir-parse-qs)

A library to parse FHIR query strings.

- Validates type and returns correct object
- Built-in search parameters from FHIR standard
- Supports modifiers, prefixes, and chains

Releases 0.7.x and below used FHIR R3. Releases 0.8.x and greater use FHIR R4.

The `update_mappings.py` script generates the mappings from the [HL7
releases](https://www.hl7.org/fhir/).

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

    # iterate over the parameter/value pairs
    for x in search:
         print(x) --> FHIRSearch(...)

    # ignores and logs unrecognized parameters
    search = Search('Patient', 'random=test')
    search.error --> [...]

    # supports chains (list of lists)
    search = Search('Observation', 'patient.name=peter')
    search[0].parameter --> 'name' # last parameter in chain
    search[0].value --> 'peter'
    search[0].chain --> [[FHIRChain(...), FHIRChain(...)], ...]
    search[0].chain[0][0].endpoint = 'Observation'
    search[0].chain[0][0].target = 'patient'
    search[0].chain[0][0].ttype = 'reference'
    search[0].chain[0][1].endpoint = 'Patient'
    search[0].chain[0][1].target = 'name'
    search[0].chain[0][1].ttype = 'string'

    # return control parameters (eg, _sort, _count, etc)
    search.control --> [...]
