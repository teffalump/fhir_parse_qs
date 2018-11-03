__all__=['diagnosticreport_mapping', 'diagnosticreport_references']

diagnosticreport_mapping = {
    'code': 'token',
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'encounter': 'reference',
    'based-on': 'reference',
    'category': 'token',
    'context': 'reference',
    'diagnosis': 'token',
    'image': 'reference',
    'issued': 'date',
    'performer': 'reference',
    'result': 'reference',
    'specimen': 'reference',
    'status': 'token',
    'subject': 'reference',
    }

diagnosticreport_references = {
    'patient': [ 'Patient' ],
    'encounter': [ 'Encounter' ],
    'based-on': [ 'ReferralRequest', 'CarePlan', 'MedicationRequest', 'NutritionOrder', 'ProcedureRequest', 'ImmunizationRecommendation' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'image': [ 'Media' ],
    'performer': [ 'Practitioner', 'Organization' ],
    'result': [ 'Observation' ],
    'specimen': [ 'Specimen' ],
    'subject': [ 'Group', 'Device', 'Patient', 'Location' ],
    }
