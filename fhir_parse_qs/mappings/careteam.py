__all__=['careteam_mapping', 'careteam_references']

careteam_mapping = {
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'category': 'token',
    'context': 'reference',
    'encounter': 'reference',
    'participant': 'reference',
    'status': 'token',
    'subject': 'reference',
    }

careteam_references = {
    'patient': [ 'Patient' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'encounter': [ 'Encounter' ],
    'participant': [ 'Practitioner', 'Organization', 'CareTeam', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
