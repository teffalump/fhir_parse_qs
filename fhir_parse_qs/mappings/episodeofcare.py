__all__=['episodeofcare_mapping', 'episodeofcare_references']

episodeofcare_mapping = {
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'type': 'token',
    'care-manager': 'reference',
    'condition': 'reference',
    'incomingreferral': 'reference',
    'organization': 'reference',
    'status': 'token',
    }

episodeofcare_references = {
    'patient': [ 'Patient' ],
    'care-manager': [ 'Practitioner' ],
    'condition': [ 'Condition' ],
    'incomingreferral': [ 'ReferralRequest' ],
    'organization': [ 'Organization' ],
    }
