mapping = {
        'date':  'date',
        'dose-sequence':  'number',
        'identifier':  'token',
        'location':  'reference',
        'lot-number':  'string',
        'manufacturer':  'reference',
        'notgiven':  'token',
        'patient':  'reference',
        'practitioner':  'reference',
        'reaction':  'reference',
        'reaction-date':  'date',
        'reason':  'token',
        'reason-not-given':  'token',
        'status':  'token',
        'vaccine-code':  'token',
        }

immunization = {
        'location': ['Location'],
        'manufacturer': ['Organization'],
        'patient': ['Patient'],
        'practitioner': ['Practitioner'],
        'reaction': ['Observation'],
        }
