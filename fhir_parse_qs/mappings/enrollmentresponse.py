__all__=['enrollmentresponse_mapping', 'enrollmentresponse_references']

enrollmentresponse_mapping = {
    'identifier': 'token',
    'organization': 'reference',
    'request': 'reference',
    }

enrollmentresponse_references = {
    'organization': [ 'Organization' ],
    'request': [ 'EnrollmentRequest' ],
    }
