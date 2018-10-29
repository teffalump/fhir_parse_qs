mapping = {
        'care-team': 'reference',
        'created': 'date',
        'encounter': 'reference',
        'enterer': 'reference',
        'facility': 'reference',
        'identifier': 'token',
        'insurer': 'reference',
        'organization': 'reference',
        'patient': 'reference',
        'payee': 'reference',
        'priority': 'token',
        'provider': 'reference',
        'use': 'token',
        }

references = {
        'care-team': ['Practitioner', 'Organization'],
        'encounter': ['Encounter'],
        'enterer': ['Practitioner'],
        'facility': ['Location'],
        'insurer': ['Organization'],
        'organization': ['Organization'],
        'patient': ['Patient'],
        'payee': ['Practitioner', 'Organization', 'Patient', 'RelatedPerson'],
        'provider': ['Practitioner'],
        }
