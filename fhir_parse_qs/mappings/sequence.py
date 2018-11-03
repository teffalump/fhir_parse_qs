__all__=['sequence_mapping', 'sequence_references']

sequence_mapping = {
    'chromosome': 'token',
    'coordinate': 'composite',
    'end': 'number',
    'identifier': 'token',
    'patient': 'reference',
    'start': 'number',
    'type': 'token',
    }

sequence_references = {
    'patient': [ 'Patient' ],
    }
