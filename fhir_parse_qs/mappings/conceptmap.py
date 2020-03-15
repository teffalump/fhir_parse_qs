__all__ = ["conceptmap_mapping", "conceptmap_references"]

conceptmap_mapping = {
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
    "dependson": "uri",
    "other": "reference",
    "product": "uri",
    "source": "reference",
    "source-code": "token",
    "source-system": "uri",
    "source-uri": "reference",
    "target": "reference",
    "target-code": "token",
    "target-system": "uri",
    "target-uri": "reference",
}

conceptmap_references = {
    "other": ["ConceptMap"],
    "source": ["ValueSet"],
    "source-uri": ["ValueSet"],
    "target": ["ValueSet"],
    "target-uri": ["ValueSet"],
}
