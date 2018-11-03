__all__=['conceptmap_mapping', 'conceptmap_references']

conceptmap_mapping = {
    'date': 'date',
    'dependson': 'uri',
    'description': 'string',
    'identifier': 'token',
    'jurisdiction': 'token',
    'name': 'string',
    'other': 'uri',
    'product': 'uri',
    'publisher': 'string',
    'source': 'reference',
    'source-code': 'token',
    'source-system': 'uri',
    'source-uri': 'reference',
    'status': 'token',
    'target': 'reference',
    'target-code': 'token',
    'target-system': 'uri',
    'target-uri': 'reference',
    'title': 'string',
    'url': 'uri',
    'version': 'token',
    }

conceptmap_references = {
    'source': [ 'ValueSet' ],
    'source-uri': [ 'ValueSet' ],
    'target': [ 'ValueSet' ],
    'target-uri': [ 'ValueSet' ],
    }
