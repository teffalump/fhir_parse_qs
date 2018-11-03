__all__=['processrequest_mapping', 'processrequest_references']

processrequest_mapping = {
    'action': 'token',
    'identifier': 'token',
    'organization': 'reference',
    'provider': 'reference',
    }

processrequest_references = {
    'organization': [ 'Organization' ],
    'provider': [ 'Practitioner' ],
    }
