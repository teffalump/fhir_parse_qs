mapping = {
        'based-on': 'reference',
        'category': 'token',
        'code': 'token',
        'context':  'reference',
        'date':  'date',
        'definition': 'reference',
        'encounter': 'reference',
        'identifier': 'token',
        'location': 'reference',
        'part-of': 'reference',
        'patient': 'reference',
        'performer': 'reference',
        'status': 'token',
        'subject': 'reference',
        }

references = {
        'based-on': ['ReferralRequest', 'CarePlan', 'ProcedureRequest'],
        'context': ['EpisodeOfCare', 'Encounter'],
        'definition': ['PlanDefinition', 'HealthcareService', 'ActivityDefinition'],
        'encounter': ['Encounter'],
        'location': ['Location'],
        'part-of': ['Observation', 'Procedure', 'MedicationAdministration'],
        'patient': ['Patient'],
        'performer': ['Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson'],
        'subject': ['Group', 'Patient'],
        }
