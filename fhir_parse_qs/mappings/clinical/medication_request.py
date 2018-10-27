mapping = {
        'authoredon':  'date',
        'category':  'token',
        'code':  'token',
        'context':  'reference',
        'date':  'date',
        'identifier':  'token',
        'intended-dispenser':  'reference',
        'intent':  'token',
        'medication':  'reference',
        'patient':  'reference',
        'priority':  'token',
        'requester':  'reference',
        'status':  'token',
        'subject':  'reference',
        }

references = {
        'context': ['EpisodeOfCare', 'Encounter'],
        'intended-dispenser': ['Organization'],
        'medication': ['Medication'],
        'patient': ['Patient'],
        'requester': ['Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson'],
        'subject': ['Group', 'Patient'],
        }
