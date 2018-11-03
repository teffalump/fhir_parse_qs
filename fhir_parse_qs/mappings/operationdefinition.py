__all__=['operationdefinition_mapping', 'operationdefinition_references']

operationdefinition_mapping = {
    'base': 'reference',
    'code': 'token',
    'date': 'date',
    'description': 'string',
    'instance': 'token',
    'jurisdiction': 'token',
    'kind': 'token',
    'name': 'string',
    'param-profile': 'reference',
    'publisher': 'string',
    'status': 'token',
    'system': 'token',
    'type': 'token',
    'url': 'uri',
    'version': 'token',
    }

operationdefinition_references = {
    'base': [ 'OperationDefinition' ],
    'param-profile': [ 'StructureDefinition' ],
    }
