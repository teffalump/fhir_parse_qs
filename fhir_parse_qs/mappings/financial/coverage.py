mapping = {
        'beneficiary': 'reference',
        'class': 'string',
        'dependent': 'string',
        'group': 'string',
        'identifier': 'token',
        'payor': 'reference',
        'plan': 'string',
        'policy-holder': 'reference',
        'sequence': 'string',
        'subclass': 'string',
        'subgroup': 'string',
        'subplan': 'string',
        'subscriber': 'reference',
        'type': 'token',
        }

references = {
        'beneficiary': ['Patient'],
        'payor': ['Organization', 'Patient', 'RelatedPerson'],
        'policy-holder': ['Organization', 'Patient', 'RelatedPerson'],
        'subscriber': ['Patient', 'RelatedPerson'],
        }
