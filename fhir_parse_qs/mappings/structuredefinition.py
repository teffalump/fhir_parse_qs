__all__ = ["structuredefinition_mapping", "structuredefinition_references"]

structuredefinition_mapping = {
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
    "identifier": "token",
    "abstract": "token",
    "base": "reference",
    "base-path": "token",
    "derivation": "token",
    "experimental": "token",
    "ext-context": "token",
    "keyword": "token",
    "kind": "token",
    "path": "token",
    "type": "uri",
    "valueset": "reference",
}

structuredefinition_references = {
    "base": ["StructureDefinition"],
    "valueset": ["ValueSet"],
}
