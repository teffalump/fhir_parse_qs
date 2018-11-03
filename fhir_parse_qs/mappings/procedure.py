__all__=['procedure_mapping', 'procedure_references']

procedure_mapping = {
    'code': 'token',
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'encounter': 'reference',
    'based-on': 'reference',
    'category': 'token',
    'context': 'reference',
    'definition': 'reference',
    'location': 'reference',
    'part-of': 'reference',
    'performer': 'reference',
    'status': 'token',
    'subject': 'reference',
    }

procedure_references = {
    'patient': [ 'Patient' ],
    'encounter': [ 'Encounter' ],
    'based-on': [ 'ReferralRequest', 'CarePlan', 'ProcedureRequest' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'definition': [ 'PlanDefinition', 'HealthcareService', 'ActivityDefinition' ],
    'location': [ 'Location' ],
    'part-of': [ 'Observation', 'Procedure', 'MedicationAdministration' ],
    'performer': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
