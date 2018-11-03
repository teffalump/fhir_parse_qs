__all__=['explanationofbenefit_mapping', 'explanationofbenefit_references']

explanationofbenefit_mapping = {
    'care-team': 'reference',
    'claim': 'reference',
    'coverage': 'reference',
    'created': 'date',
    'disposition': 'string',
    'encounter': 'reference',
    'enterer': 'reference',
    'facility': 'reference',
    'identifier': 'token',
    'organization': 'reference',
    'patient': 'reference',
    'payee': 'reference',
    'provider': 'reference',
    }

explanationofbenefit_references = {
    'care-team': [ 'Practitioner', 'Organization' ],
    'claim': [ 'Claim' ],
    'coverage': [ 'Coverage' ],
    'encounter': [ 'Encounter' ],
    'enterer': [ 'Practitioner' ],
    'facility': [ 'Location' ],
    'organization': [ 'Organization' ],
    'patient': [ 'Patient' ],
    'payee': [ 'Practitioner', 'Organization', 'Patient', 'RelatedPerson' ],
    'provider': [ 'Practitioner' ],
    }
