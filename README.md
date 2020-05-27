# fhir_parse_qs

[![Build Status](https://travis-ci.com/teffalump/fhir_parse_qs.svg?branch=master)](https://travis-ci.com/teffalump/fhir_parse_qs)
[![PyPI version](https://badge.fury.io/py/fhir-parse-qs.svg)](https://badge.fury.io/py/fhir-parse-qs)

A library to parse FHIR query strings.

- Validates type and returns correct object
- Built-in search parameters from FHIR standard
- Supports modifiers, prefixes, and chains

Releases 0.7.x and below used FHIR R3. Releases 0.8.x and greater use FHIR R4.

The `update_mappings.py` script generates the mappings from the [HL7 FHIR releases](https://www.hl7.org/fhir/).

#### Usage

    from fhir_parse_qs import Search

    # supported endpoints
    Search.supported ==> [...]

    # simple use
    search = Search('Patient', 'name=bob') # Search(<endpoint>, <query_string>)

    # endpoint
    search.endpoint ==> 'Patient'

    # all the namedtuples
    search.parsed ==> [FHIRSearchPair(...)]

    # index as key; each parameter/value pair s parsed into a namedtuple
    search[0] ==> FHIRSearchPair(...)
    search[0].modifier ==> None
    search[0].prefix ==> None
    search[0].value ==> 'bob'
    search[0].parameter ==> 'name'
    search[0].type_ ==> 'string'
    search[0].chain ==> None

    # act like dict with parameter as key
    search['name'] ==> FHIRSearchPair(...) #list if non-unique parameter

    # iterate over the parameter/value pairs
    for x in search:
         print(x) ==> FHIRSearchPair(...)

    # ignores and logs unrecognized parameters
    search = Search('Patient', 'random=test')
    search.error ==> [...]

    # supports chains (list of lists)
    search = Search('Observation', 'patient.name=peter')
    search[0].parameter ==> 'name' # last parameter in chain
    search[0].value ==> 'peter'
    search[0].chain ==> [[FHIRChain(...), FHIRChain(...)], ...]
    search[0].chain[0][0].endpoint ==> 'Observation'
    search[0].chain[0][0].tar ==> 'patient'
    search[0].chain[0][0].ttype ==> 'reference'
    search[0].chain[0][1].endpoint ==> 'Patient'
    search[0].chain[0][1].tar ==> 'name'
    search[0].chain[0][1].ttype ==> 'string'

    # supports systems and codes
    search = Search("Observation", "value-quantity=gt234|http://loinc.org|mg")
    search["value-quantity"].value ==> 234
    search["value-quantity"].prefix ==> "gt"
    search["value-quantity"].system ==> "http://loinc.org"
    search["value-quantity"].code ==> "mg"

    # return control parameters (eg, _sort, _count, etc)
    search.control ==> [...]

#### TODO

- Narrow allowed chains (return error for ambiguous chains)
- The `_filter` parameter
- Reverse chains
- Composite searches
