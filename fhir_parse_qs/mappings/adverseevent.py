__all__=['adverseevent_mapping', 'adverseevent_references']

adverseevent_mapping = {
    'category': 'token',
    'date': 'date',
    'location': 'reference',
    'reaction': 'reference',
    'recorder': 'reference',
    'seriousness': 'token',
    'study': 'reference',
    'subject': 'reference',
    'substance': 'reference',
    'type': 'token',
    }

adverseevent_references = {
    'location': [ 'Location' ],
    'reaction': [ 'Condition' ],
    'recorder': [ 'Practitioner', 'Patient', 'RelatedPerson' ],
    'study': [ 'ResearchStudy' ],
    'subject': [ 'Device', 'Medication', 'Patient', 'ResearchSubject' ],
    'substance': [ 'Device', 'Medication', 'Substance', 'MedicationAdministration', 'MedicationStatement' ],
    }
