__all__ = ["researchstudy_mapping", "researchstudy_references"]

researchstudy_mapping = {
    "category": "token",
    "date": "date",
    "focus": "token",
    "identifier": "token",
    "keyword": "token",
    "location": "token",
    "partof": "reference",
    "principalinvestigator": "reference",
    "protocol": "reference",
    "site": "reference",
    "sponsor": "reference",
    "status": "token",
    "title": "string",
}

researchstudy_references = {
    "partof": ["ResearchStudy"],
    "principalinvestigator": ["Practitioner", "PractitionerRole"],
    "protocol": ["PlanDefinition"],
    "site": ["Location"],
    "sponsor": ["Organization"],
}
