__all__=['namingsystem_mapping', 'namingsystem_references']

namingsystem_mapping = {
    'contact': 'string',
    'date': 'date',
    'description': 'string',
    'id-type': 'token',
    'jurisdiction': 'token',
    'kind': 'token',
    'name': 'string',
    'period': 'date',
    'publisher': 'string',
    'replaced-by': 'reference',
    'responsible': 'string',
    'status': 'token',
    'telecom': 'token',
    'type': 'token',
    'value': 'string',
    }

namingsystem_references = {
    'replaced-by': [ 'NamingSystem' ],
    }
