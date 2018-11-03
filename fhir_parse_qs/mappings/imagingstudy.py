__all__=['imagingstudy_mapping', 'imagingstudy_references']

imagingstudy_mapping = {
    'identifier': 'token',
    'patient': 'reference',
    'accession': 'token',
    'basedon': 'reference',
    'bodysite': 'token',
    'context': 'reference',
    'dicom-class': 'uri',
    'endpoint': 'reference',
    'modality': 'token',
    'performer': 'reference',
    'reason': 'token',
    'series': 'uri',
    'started': 'date',
    'study': 'uri',
    'uid': 'uri',
    }

imagingstudy_references = {
    'patient': [ 'Patient' ],
    'basedon': [ 'ReferralRequest', 'CarePlan', 'ProcedureRequest' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'endpoint': [ 'Endpoint' ],
    'performer': [ 'Practitioner' ],
    }
