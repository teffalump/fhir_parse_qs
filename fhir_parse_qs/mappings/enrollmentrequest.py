__all__=['enrollmentrequest_mapping', 'enrollmentrequest_references']

enrollmentrequest_mapping = {
    'identifier': 'token',
    'organization': 'reference',
    'patient': 'reference',
    'subject': 'reference',
    }

enrollmentrequest_references = {
    'organization': [ 'Organization' ],
    'patient': [ 'Patient' ],
    'subject': [ 'Patient' ],
    }
