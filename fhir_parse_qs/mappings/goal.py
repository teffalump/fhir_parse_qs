__all__=['goal_mapping', 'goal_references']

goal_mapping = {
    'identifier': 'token',
    'patient': 'reference',
    'category': 'token',
    'start-date': 'date',
    'status': 'token',
    'subject': 'reference',
    'target-date': 'date',
    }

goal_references = {
    'patient': [ 'Patient' ],
    'subject': [ 'Group', 'Organization', 'Patient' ],
    }
