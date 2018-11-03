__all__=['visionprescription_mapping', 'visionprescription_references']

visionprescription_mapping = {
    'identifier': 'token',
    'patient': 'reference',
    'encounter': 'reference',
    'datewritten': 'date',
    'prescriber': 'reference',
    }

visionprescription_references = {
    'patient': [ 'Patient' ],
    'encounter': [ 'Encounter' ],
    'prescriber': [ 'Practitioner' ],
    }
