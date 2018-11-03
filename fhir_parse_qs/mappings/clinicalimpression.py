__all__=['clinicalimpression_mapping', 'clinicalimpression_references']

clinicalimpression_mapping = {
    'date': 'date',
    'patient': 'reference',
    'action': 'reference',
    'assessor': 'reference',
    'context': 'reference',
    'finding-code': 'token',
    'finding-ref': 'reference',
    'identifier': 'token',
    'investigation': 'reference',
    'previous': 'reference',
    'problem': 'reference',
    'status': 'token',
    'subject': 'reference',
    }

clinicalimpression_references = {
    'patient': [ 'Patient' ],
    'action': [ 'Appointment', 'ReferralRequest', 'MedicationRequest', 'ProcedureRequest', 'Procedure' ],
    'assessor': [ 'Practitioner' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'finding-ref': [ 'Condition', 'Observation' ],
    'investigation': [ 'RiskAssessment', 'FamilyMemberHistory', 'Observation', 'DiagnosticReport', 'ImagingStudy', 'QuestionnaireResponse' ],
    'previous': [ 'ClinicalImpression' ],
    'problem': [ 'Condition', 'AllergyIntolerance' ],
    'subject': [ 'Group', 'Patient' ],
    }
