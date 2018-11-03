__all__=['structuredefinition_mapping', 'structuredefinition_references']

structuredefinition_mapping = {
    'abstract': 'token',
    'base': 'uri',
    'base-path': 'token',
    'context-type': 'token',
    'date': 'date',
    'derivation': 'token',
    'description': 'string',
    'experimental': 'token',
    'ext-context': 'string',
    'identifier': 'token',
    'jurisdiction': 'token',
    'keyword': 'token',
    'kind': 'token',
    'name': 'string',
    'path': 'token',
    'publisher': 'string',
    'status': 'token',
    'title': 'string',
    'type': 'token',
    'url': 'uri',
    'valueset': 'reference',
    'version': 'token',
    }

structuredefinition_references = {
    'valueset': [ 'ValueSet' ],
    }
