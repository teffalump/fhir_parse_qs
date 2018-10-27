mapping = {
        'authored':  'date',
        'based-on':  'reference',
        'body-site':  'token',
        'code':  'token',
        'context':  'reference',
        'definition':  'reference',
        'encounter':  'reference',
        'identifier':  'token',
        'intent':  'token',
        'occurrence':  'date',
        'patient':  'reference',
        'performer':  'reference',
        'performer-type':  'token',
        'priority':  'token',
        'replaces':  'reference',
        'requester':  'reference',
        'requisition':  'token',
        'specimen':  'reference',
        'status':  'token',
        'subject':  'reference',
        }

references = {
        'based-on': [], #ANY????
        'context': ['EpisodeOfCare', 'Encounter'],
        'definition': ['PlanDefinition', 'ActivityDefinition'],
        'encounter': ['Encounter'],
        'patient': ['Patient'],
        'performer': ['Practitioner', 'Organization', 'Device', 'Patient', 'HealthcareService', 'RelatedPerson'],
        'replaces': [], #ANY???
        'requester': ['Practitioner', 'Organization', 'Device'],
        'specimen': ['Specimen'],
        'subject': ['Group', 'Device', 'Patient', 'Location'],
        }
