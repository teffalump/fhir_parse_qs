__all__=['referralrequest_mapping', 'referralrequest_references']

referralrequest_mapping = {
    'patient': 'reference',
    'type': 'token',
    'authored-on': 'date',
    'based-on': 'reference',
    'context': 'reference',
    'definition': 'reference',
    'encounter': 'reference',
    'group-identifier': 'token',
    'identifier': 'token',
    'intent': 'token',
    'occurrence-date': 'date',
    'priority': 'token',
    'recipient': 'reference',
    'replaces': 'reference',
    'requester': 'reference',
    'service': 'token',
    'specialty': 'token',
    'status': 'token',
    'subject': 'reference',
    }

referralrequest_references = {
    'patient': [ 'Patient' ],
    'based-on': [ 'ReferralRequest', 'CarePlan', 'ProcedureRequest' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'definition': [ 'PlanDefinition', 'ActivityDefinition' ],
    'encounter': [ 'Encounter' ],
    'recipient': [ 'Practitioner', 'Organization', 'HealthcareService' ],
    'replaces': [ 'ReferralRequest' ],
    'requester': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
