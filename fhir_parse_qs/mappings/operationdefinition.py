__all__ = ["operationdefinition_mapping", "operationdefinition_references"]

operationdefinition_mapping = {
    "context": "token",
    "context-quantity": "quantity",
    "context-type": "token",
    "date": "date",
    "description": "string",
    "jurisdiction": "token",
    "name": "string",
    "publisher": "string",
    "status": "token",
    "title": "string",
    "url": "uri",
    "version": "token",
    "context-type-quantity": "composite",
    "context-type-value": "composite",
    "base": "reference",
    "code": "token",
    "input-profile": "reference",
    "instance": "token",
    "kind": "token",
    "output-profile": "reference",
    "system": "token",
    "type": "token",
}

operationdefinition_references = {
    "base": ["OperationDefinition"],
    "input-profile": ["StructureDefinition"],
    "output-profile": ["StructureDefinition"],
}
