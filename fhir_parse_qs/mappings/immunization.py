__all__=['immunization_mapping', 'immunization_references']

immunization_mapping = {
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'dose-sequence': 'number',
    'location': 'reference',
    'lot-number': 'string',
    'manufacturer': 'reference',
    'notgiven': 'token',
    'practitioner': 'reference',
    'reaction': 'reference',
    'reaction-date': 'date',
    'reason': 'token',
    'reason-not-given': 'token',
    'status': 'token',
    'vaccine-code': 'token',
    }

immunization_references = {
    'patient': [ 'Patient' ],
    'location': [ 'Location' ],
    'manufacturer': [ 'Organization' ],
    'practitioner': [ 'Practitioner' ],
    'reaction': [ 'Observation' ],
    }
