__all__=['eligibilityresponse_mapping', 'eligibilityresponse_references']

eligibilityresponse_mapping = {
    'created': 'date',
    'disposition': 'string',
    'identifier': 'token',
    'insurer': 'reference',
    'outcome': 'token',
    'request': 'reference',
    'request-organization': 'reference',
    'request-provider': 'reference',
    }

eligibilityresponse_references = {
    'insurer': [ 'Organization' ],
    'request': [ 'EligibilityRequest' ],
    'request-organization': [ 'Organization' ],
    'request-provider': [ 'Practitioner' ],
    }
