mapping = {
        'code':  'token',
        'context':  'reference',
        'destination':  'reference',
        'identifier':  'token',
        'medication':  'reference',
        'patient':  'reference',
        'performer':  'reference',
        'prescription':  'reference',
        'receiver':  'reference',
        'responsibleparty':  'reference',
        'status':  'token',
        'subject':  'reference',
        'type':  'token',
        'whenhandedover':  'date',
        'whenprepared':  'date',
        }

references = {
        'context': ['EpisodeOfCare', 'Encounter'],
        'destination': ['Location'],
        'medication': ['Medication'],
        'patient': ['Patient'],
        'performer': ['Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson'],
        'prescription': ['MedicationRequest'],
        'receiver': ['Practitioner', 'Patient'],
        'responsibleparty': ['Practitioner'],
        'subject': ['Group', 'Patient'],
        }
