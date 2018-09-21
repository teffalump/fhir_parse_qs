mapping = {
        'category':  'token',
        'code':  'token',
        'context':  'reference',
        'effective':  'date',
        'identifier':  'token',
        'medication':  'reference',
        'part-of':  'reference',
        'patient':  'reference',
        'source':  'reference',
        'status':  'token',
        'subject':  'reference',
        }

references = {
        'context': ['EpisodeOfCare', 'Encounter'],
        'medication': ['Medication'],
        'part-of': ['MedicationDispense', 'Observation', 'MedicationAdministration', 'Procedure', 'MedicationStatement'],
        'patient': ['Patient'],
        'source': ['Practitioner', 'Organization', 'Patient', 'RelatedPerson'],
        'subject': ['Group', 'Patient'],
        }
