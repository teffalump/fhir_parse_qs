__all__=['nutritionorder_mapping', 'nutritionorder_references']

nutritionorder_mapping = {
    'identifier': 'token',
    'patient': 'reference',
    'encounter': 'reference',
    'additive': 'token',
    'datetime': 'date',
    'formula': 'token',
    'oraldiet': 'token',
    'provider': 'reference',
    'status': 'token',
    'supplement': 'token',
    }

nutritionorder_references = {
    'patient': [ 'Patient' ],
    'encounter': [ 'Encounter' ],
    'provider': [ 'Practitioner' ],
    }
