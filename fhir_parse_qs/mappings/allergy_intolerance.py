mapping = {
        'asserter':  'reference',
        'category':  'token',
        'clinical-status':  'token',
        'code':  'token',
        'criticality':  'token',
        'date':  'date',
        'identifier':  'token',
        'last-date':  'date',
        'manifestation':  'token',
        'onset':  'date',
        'patient':  'reference',
        'recorder':  'reference',
        'route':  'token',
        'severity':  'token',
        'type':  'token',
        'verification-status':  'token',
        }

references = {
        'asserter': ['Patient', 'Practitioner', 'RelatedPerson'],
        'patient': ['Patient'],
        'recorder': ['Patient', 'Practitioner'],
        }
