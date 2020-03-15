__all__ = ["messagedefinition_mapping", "messagedefinition_references"]

messagedefinition_mapping = {
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
    "category": "token",
    "event": "token",
    "focus": "token",
    "parent": "reference",
}

messagedefinition_references = {
    "parent": ["PlanDefinition", "ActivityDefinition"],
}
