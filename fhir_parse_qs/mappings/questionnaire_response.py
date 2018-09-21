mapping = {
        'author':  'reference',
        'authored':  'date',
        'based-on':  'reference',
        'context':  'reference',
        'identifier':  'token',
        'parent':  'reference',
        'patient':  'reference',
        'questionnaire':  'reference',
        'source':  'reference',
        'status':  'token',
        'subject':  'reference',
        }

references = {
        'author': ['Practitioner', 'Device', 'Patient', 'RelatedPerson'],
        'based-on': ['ReferralRequest', 'CarePlan', 'ProcedureRequest'],
        'context': ['EpisodeOfCare', 'Encounter'],
        'parent': ['Observation', 'Procedure'],
        'patient': ['Patient'],
        'questionnaire': ['Questionnaire'],
        'source': ['Practitioner', 'Patient', 'RelatedPerson'],
        }
