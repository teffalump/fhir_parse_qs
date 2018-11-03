__all__=['claimresponse_mapping', 'claimresponse_references']

claimresponse_mapping = {
    'created': 'date',
    'disposition': 'string',
    'identifier': 'token',
    'insurer': 'reference',
    'outcome': 'token',
    'patient': 'reference',
    'payment-date': 'date',
    'request': 'reference',
    'request-provider': 'reference',
    }

claimresponse_references = {
    'insurer': [ 'Organization' ],
    'patient': [ 'Patient' ],
    'request': [ 'Claim' ],
    'request-provider': [ 'Practitioner' ],
    }
