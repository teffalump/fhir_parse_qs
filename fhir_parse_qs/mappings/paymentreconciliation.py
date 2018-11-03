__all__=['paymentreconciliation_mapping', 'paymentreconciliation_references']

paymentreconciliation_mapping = {
    'created': 'date',
    'disposition': 'string',
    'identifier': 'token',
    'organization': 'reference',
    'outcome': 'token',
    'request': 'reference',
    'request-organization': 'reference',
    'request-provider': 'reference',
    }

paymentreconciliation_references = {
    'organization': [ 'Organization' ],
    'request': [ 'ProcessRequest' ],
    'request-organization': [ 'Organization' ],
    'request-provider': [ 'Practitioner' ],
    }
