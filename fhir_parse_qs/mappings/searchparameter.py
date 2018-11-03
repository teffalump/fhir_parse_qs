__all__=['searchparameter_mapping', 'searchparameter_references']

searchparameter_mapping = {
    'base': 'token',
    'code': 'token',
    'component': 'reference',
    'date': 'date',
    'derived-from': 'uri',
    'description': 'string',
    'jurisdiction': 'token',
    'name': 'string',
    'publisher': 'string',
    'status': 'token',
    'target': 'token',
    'type': 'token',
    'url': 'uri',
    'version': 'token',
    }

searchparameter_references = {
    'component': [ 'SearchParameter' ],
    }
