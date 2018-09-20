mapping = {
        'accession':  'token',
        'basedon':  'reference',
        'bodysite':  'token',
        'context':  'reference',
        'dicom-class':  'uri',
        'endpoint':  'reference',
        'identifier':  'token',
        'modality':  'token',
        'patient':  'reference',
        'performer':  'reference',
        'reason':  'token',
        'series':  'uri',
        'started':  'date',
        'study':  'uri',
        'uid':  'uri',
        }

references = {
        'basedon': ['ReferralRequest', 'CarePlan', 'ProcedureRequest'],
        'context': ['EpisodeOfCare', 'Encounter'],
        'endpoint': ['Endpoint'],
        'patient': ['Patient'],
        'performer': ['Practitioner'],
        }
