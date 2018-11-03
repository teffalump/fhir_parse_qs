__all__=['medicationstatement_mapping', 'medicationstatement_references']

medicationstatement_mapping = {
    'code': 'token',
    'identifier': 'token',
    'medication': 'reference',
    'patient': 'reference',
    'status': 'token',
    'category': 'token',
    'context': 'reference',
    'effective': 'date',
    'part-of': 'reference',
    'source': 'reference',
    'subject': 'reference',
    }

medicationstatement_references = {
    'medication': [ 'Medication' ],
    'patient': [ 'Patient' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'part-of': [ 'MedicationDispense', 'Observation', 'MedicationAdministration', 'Procedure', 'MedicationStatement' ],
    'source': [ 'Practitioner', 'Organization', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
