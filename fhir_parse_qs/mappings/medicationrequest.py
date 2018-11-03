__all__=['medicationrequest_mapping', 'medicationrequest_references']

medicationrequest_mapping = {
    'code': 'token',
    'identifier': 'token',
    'medication': 'reference',
    'patient': 'reference',
    'status': 'token',
    'authoredon': 'date',
    'category': 'token',
    'context': 'reference',
    'date': 'date',
    'intended-dispenser': 'reference',
    'intent': 'token',
    'priority': 'token',
    'requester': 'reference',
    'subject': 'reference',
    }

medicationrequest_references = {
    'medication': [ 'Medication' ],
    'patient': [ 'Patient' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'intended-dispenser': [ 'Organization' ],
    'requester': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
