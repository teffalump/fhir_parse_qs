__all__ = ["familymemberhistory_mapping", "familymemberhistory_references"]

familymemberhistory_mapping = {
    "code": "token",
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "instantiates-canonical": "reference",
    "instantiates-uri": "uri",
    "relationship": "token",
    "sex": "token",
    "status": "token",
}

familymemberhistory_references = {
    "patient": ["Patient"],
    "instantiates-canonical": [
        "Questionnaire",
        "Measure",
        "PlanDefinition",
        "OperationDefinition",
        "ActivityDefinition",
    ],
}
