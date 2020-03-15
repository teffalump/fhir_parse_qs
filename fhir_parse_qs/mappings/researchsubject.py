__all__ = ["researchsubject_mapping", "researchsubject_references"]

researchsubject_mapping = {
    "date": "date",
    "identifier": "token",
    "individual": "reference",
    "patient": "reference",
    "status": "token",
    "study": "reference",
}

researchsubject_references = {
    "individual": ["Patient"],
    "patient": ["Patient"],
    "study": ["ResearchStudy"],
}
