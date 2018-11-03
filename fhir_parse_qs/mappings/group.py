__all__=['group_mapping', 'group_references']

group_mapping = {
    'actual': 'token',
    'characteristic': 'token',
    'characteristic-value': 'composite',
    'code': 'token',
    'exclude': 'token',
    'identifier': 'token',
    'member': 'reference',
    'type': 'token',
    'value': 'token',
    }

group_references = {
    'member': [ 'Practitioner', 'Device', 'Medication', 'Patient', 'Substance' ],
    }
