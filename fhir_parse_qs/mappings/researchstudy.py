__all__=['researchstudy_mapping', 'researchstudy_references']

researchstudy_mapping = {
    'category': 'token',
    'date': 'date',
    'focus': 'token',
    'identifier': 'token',
    'jurisdiction': 'token',
    'keyword': 'token',
    'partof': 'reference',
    'principalinvestigator': 'reference',
    'protocol': 'reference',
    'site': 'reference',
    'sponsor': 'reference',
    'status': 'token',
    'title': 'string',
    }

researchstudy_references = {
    'partof': [ 'ResearchStudy' ],
    'principalinvestigator': [ 'Practitioner' ],
    'protocol': [ 'PlanDefinition' ],
    'site': [ 'Location' ],
    'sponsor': [ 'Organization' ],
    }
