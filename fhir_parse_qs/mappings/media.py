__all__=['media_mapping', 'media_references']

media_mapping = {
    'based-on': 'reference',
    'context': 'reference',
    'created': 'date',
    'date': 'date',
    'device': 'reference',
    'identifier': 'token',
    'operator': 'reference',
    'patient': 'reference',
    'site': 'token',
    'subject': 'reference',
    'subtype': 'token',
    'type': 'token',
    'view': 'token',
    }

media_references = {
    'based-on': [ 'ProcedureRequest' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'device': [ 'Device', 'DeviceMetric' ],
    'operator': [ 'Practitioner' ],
    'patient': [ 'Patient' ],
    'subject': [ 'Practitioner', 'Group', 'Specimen', 'Device', 'Patient' ],
    }
