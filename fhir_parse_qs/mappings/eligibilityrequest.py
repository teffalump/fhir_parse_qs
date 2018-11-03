__all__=['eligibilityrequest_mapping', 'eligibilityrequest_references']

eligibilityrequest_mapping = {
    'created': 'date',
    'enterer': 'reference',
    'facility': 'reference',
    'identifier': 'token',
    'organization': 'reference',
    'patient': 'reference',
    'provider': 'reference',
    }

eligibilityrequest_references = {
    'enterer': [ 'Practitioner' ],
    'facility': [ 'Location' ],
    'organization': [ 'Organization' ],
    'patient': [ 'Patient' ],
    'provider': [ 'Practitioner' ],
    }
