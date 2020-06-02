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

Provide the endpoint and query_string arguments:

    from fhir_parse_qs import Search
    search = Search('Patient', 'name=bob') # Search(<endpoint>, <query_string>)

    # supported endpoints
    Search.supported ==> [...]

    # endpoint
    search.endpoint ==> 'Patient'

Each parameter/value pair is parsed into a FHIRSearchPair with attached FHIRParameter and FHIRValue namedtuples.

    # all the namedtuples
    search.parsed ==> [FHIRSearchPair(...)]

    FHIRSearchPair.parameter ==> FHIRParameter
    FHIRSearchPair.value ==> [FHIRValue, ...]

        FHIRParameter:
            value
            modifier
            chain
                [FHIRChain...]
            type_

            FHIRChain:
                endpoint
                target
                ttype

        FHIRValue:
            value
            prefix
            system
            code

Further features:

    # index as key; each parameter/value pair parsed into a namedtuple
    search[0] ==> FHIRSearchPair:
        parameter ==> FHIRParameter:
            value ==> 'name'
            modifier ==> None
            chain ==> None
            type_ ==> 'string'
        value ==> [FHIRValue(
            prefix ==> None
            value ==> 'bob'
            system ==> None
            code ==> None
            ]

    # act like dict with parameter as key
    search['name'] ==> FHIRSearchPair(...) #list if non-unique parameter

    # iterate over the parameter/value pairs
    for x in search:
         print(x) ==> FHIRSearchPair(...)

    # supports comma-separated list of values
    search = Search('Patient', 'name=peter,travis')
    search["name"] ==> [FHIRValue(...), FHIRValue(...)]

    # ignores and logs unrecognized parameters
    search = Search('Patient', 'random=test')
    search.error ==> [...]

    # supports chaining
    search = Search('Observation', 'patient.name=peter')
    search[0].parameter.value ==> 'name' # last parameter in chain
    search[0].value[0].value ==> 'peter'
    search[0].parameter.chain ==> [FHIRChain(...), FHIRChain(...)]
    search[0].parameter.chain[0].endpoint ==> 'Observation'
    search[0].parameter.chain[0].target ==> 'patient'
    search[0].parameter.chain[0].ttype ==> 'reference'
    search[0].parameter.chain[1].endpoint ==> 'Patient'
    search[0].parameter.chain[1].target ==> 'name'
    search[0].parameter.chain[1].ttype ==> 'string'

    # supports systems and codes
    search = Search("Observation", "value-quantity=gt234|http://loinc.org|mg")
    search["value-quantity"].value[0].value ==> 234
    search["value-quantity"].value[0].prefix ==> "gt"
    search["value-quantity"].value[0].system ==> "http://loinc.org"
    search["value-quantity"].value[0].code ==> "mg"

    # return control parameters (eg, _sort, _count, etc)
    search.control ==> [...]

#### TODO

- Narrow allowed chains (return error for ambiguous chains) (unreleased)
- The `_filter` parameter
- Reverse chains
- Composite searches
