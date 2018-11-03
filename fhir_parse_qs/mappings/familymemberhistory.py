__all__=['familymemberhistory_mapping', 'familymemberhistory_references']

familymemberhistory_mapping = {
    'code': 'token',
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'definition': 'reference',
    'gender': 'token',
    'relationship': 'token',
    'status': 'token',
    }

familymemberhistory_references = {
    'patient': [ 'Patient' ],
    'definition': [ 'Questionnaire', 'PlanDefinition' ],
    }
