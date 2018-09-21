mapping = {
        'code':  'token',
        'context':  'reference',
        'device':  'reference',
        'effective-time':  'date',
        'identifier':  'token',
        'medication':  'reference',
        'not-given':  'token',
        'patient':  'reference',
        'performer':  'reference',
        'prescription':  'reference',
        'reason-given':  'token',
        'reason-not-given':  'token',
        'status':  'token',
        'subject':  'reference',
        }

references = {
        'context': ['EpisodeOfCare', 'Encounter'],
        'device': ['Device'],
        'medication': ['Medication'],
        'patient': ['Patient'],
        'performer': ['Practitioner', 'Device', 'Patient', 'RelatedPerson'],
        'prescription': ['MedicationRequest'],
        'subject': ['Group', 'Patient'],
        }
