__all__ = ["capabilitystatement_mapping", "capabilitystatement_references"]

capabilitystatement_mapping = {
    "context": "token",
    "context-quantity": "quantity",
    "context-type": "token",
    "date": "date",
    "description": "string",
    "fhirversion": "token",
    "format": "token",
    "guide": "reference",
    "jurisdiction": "token",
    "mode": "token",
    "name": "string",
    "publisher": "string",
    "resource": "token",
    "resource-profile": "reference",
    "security-service": "token",
    "software": "string",
    "status": "token",
    "supported-profile": "reference",
    "title": "string",
    "url": "uri",
    "version": "token",
    "context-type-quantity": "composite",
    "context-type-value": "composite",
}

capabilitystatement_references = {
    "guide": ["ImplementationGuide"],
    "resource-profile": ["StructureDefinition"],
    "supported-profile": ["StructureDefinition"],
}
