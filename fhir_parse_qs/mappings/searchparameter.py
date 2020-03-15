__all__ = ["searchparameter_mapping", "searchparameter_references"]

searchparameter_mapping = {
    "context": "token",
    "context-quantity": "quantity",
    "context-type": "token",
    "date": "date",
    "description": "string",
    "jurisdiction": "token",
    "name": "string",
    "publisher": "string",
    "status": "token",
    "url": "uri",
    "version": "token",
    "context-type-quantity": "composite",
    "context-type-value": "composite",
    "base": "token",
    "code": "token",
    "component": "reference",
    "derived-from": "reference",
    "target": "token",
    "type": "token",
}

searchparameter_references = {
    "component": ["SearchParameter"],
    "derived-from": ["SearchParameter"],
}
