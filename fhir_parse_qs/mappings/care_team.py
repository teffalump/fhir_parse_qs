mapping = {
        'category': 'token',
        'context': 'reference',
        'date': 'date',
        'encounter': 'reference',
        'identifier': 'token',
        'participant': 'reference',
        'patient': 'reference',
        'status': 'token',
        'subject': 'reference',
        }

references = {
        'context': ['EpisodeOfCare', 'Encounter'],
        'encounter': ['Encounter'],
        'participant': ['Practitioner', 'Organization', 'CareTeam', 'Patient', 'RelatedPerson'],
        'patient': ['Patient'],
        'subject': ['Group', 'Patient'],
        }
