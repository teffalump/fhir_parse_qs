__all__=['immunizationrecommendation_mapping', 'immunizationrecommendation_references']

immunizationrecommendation_mapping = {
    'date': 'date',
    'dose-number': 'number',
    'dose-sequence': 'number',
    'identifier': 'token',
    'information': 'reference',
    'patient': 'reference',
    'status': 'token',
    'support': 'reference',
    'target-disease': 'token',
    'vaccine-type': 'token',
    }

immunizationrecommendation_references = {
    'information': [ 'AllergyIntolerance', 'Observation' ],
    'patient': [ 'Patient' ],
    'support': [ 'Immunization' ],
    }
