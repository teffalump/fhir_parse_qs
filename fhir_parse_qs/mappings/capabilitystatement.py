__all__=['capabilitystatement_mapping', 'capabilitystatement_references']

capabilitystatement_mapping = {
    'date': 'date',
    'description': 'string',
    'event': 'token',
    'fhirversion': 'token',
    'format': 'token',
    'guide': 'uri',
    'jurisdiction': 'token',
    'mode': 'token',
    'name': 'string',
    'publisher': 'string',
    'resource': 'token',
    'resource-profile': 'reference',
    'security-service': 'token',
    'software': 'string',
    'status': 'token',
    'supported-profile': 'reference',
    'title': 'string',
    'url': 'uri',
    'version': 'token',
    }

capabilitystatement_references = {
    'resource-profile': [ 'StructureDefinition' ],
    'supported-profile': [ 'StructureDefinition' ],
    }
