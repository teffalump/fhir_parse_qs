__all__=['supplyrequest_mapping', 'supplyrequest_references']

supplyrequest_mapping = {
    'date': 'date',
    'identifier': 'token',
    'category': 'token',
    'requester': 'reference',
    'status': 'token',
    'supplier': 'reference',
    }

supplyrequest_references = {
    'requester': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'supplier': [ 'Organization' ],
    }
