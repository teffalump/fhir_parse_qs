mapping = {
        'balance': 'quantity',
        'identifier': 'token',
        'name': 'string',
        'owner': 'reference',
        'patient': 'reference',
        'period': 'date',
        'status': 'token',
        'subject': 'reference',
        'type': 'token',
        }

references = {
        'owner': ['Organization'],
        'patient': ['Patient'],
        'subject': ['Practitioner', 'Organization', 'Device', 'Patient', 'HealthcareService', 'Location'],
        }
