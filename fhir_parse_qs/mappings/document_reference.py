mapping = {
        'authenticator': 'reference',
        'author': 'reference',
        'class': 'token',
        'created': 'date',
        'custodian': 'reference',
        'description': 'string',
        'encounter': 'reference',
        'event': 'token',
        'facility': 'token',
        'format': 'token',
        'identifier': 'token',
        'indexed': 'date',
        'language': 'token',
        'location': 'uri',
        'patient': 'reference',
        'period': 'date',
        'related-id': 'token',
        'related-ref': 'reference',
        'relatesto': 'reference',
        'relation': 'token',
        'relationship': 'composite',
        'securitylabel': 'token',
        'setting': 'token',
        'status': 'token',
        'subject': 'reference',
        'type': 'token',
        }

references = {
        'authenticator': ['Practitioner', 'Organization'],
        'author': ['Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson'],
        'custodian': ['Organization'],
        'encounter': ['Encounter'],
        'patent': ['Patient'],
        'related-ref': [], #ANY????
        'relatesto': ['DocumentReference'],
        'subject': ['Practitioner', 'Group', 'Device', 'Patient'],
        }
