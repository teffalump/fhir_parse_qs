__all__=['medicationdispense_mapping', 'medicationdispense_references']

medicationdispense_mapping = {
    'code': 'token',
    'identifier': 'token',
    'medication': 'reference',
    'patient': 'reference',
    'prescription': 'reference',
    'status': 'token',
    'context': 'reference',
    'destination': 'reference',
    'performer': 'reference',
    'receiver': 'reference',
    'responsibleparty': 'reference',
    'subject': 'reference',
    'type': 'token',
    'whenhandedover': 'date',
    'whenprepared': 'date',
    }

medicationdispense_references = {
    'medication': [ 'Medication' ],
    'patient': [ 'Patient' ],
    'prescription': [ 'MedicationRequest' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'destination': [ 'Location' ],
    'performer': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'receiver': [ 'Practitioner', 'Patient' ],
    'responsibleparty': [ 'Practitioner' ],
    'subject': [ 'Group', 'Patient' ],
    }
