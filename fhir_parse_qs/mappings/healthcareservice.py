__all__=['healthcareservice_mapping', 'healthcareservice_references']

healthcareservice_mapping = {
    'active': 'token',
    'category': 'token',
    'characteristic': 'token',
    'endpoint': 'reference',
    'identifier': 'token',
    'location': 'reference',
    'name': 'string',
    'organization': 'reference',
    'programname': 'string',
    'type': 'token',
    }

healthcareservice_references = {
    'endpoint': [ 'Endpoint' ],
    'location': [ 'Location' ],
    'organization': [ 'Organization' ],
    }
