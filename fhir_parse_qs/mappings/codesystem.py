__all__ = ["codesystem_mapping", "codesystem_references"]

codesystem_mapping = {
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
    "code": "token",
    "content-mode": "token",
    "identifier": "token",
    "language": "token",
    "supplements": "reference",
    "system": "uri",
}

codesystem_references = {
    "supplements": ["CodeSystem"],
}
