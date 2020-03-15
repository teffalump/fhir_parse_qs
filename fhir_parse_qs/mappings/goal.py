__all__ = ["goal_mapping", "goal_references"]

goal_mapping = {
    "identifier": "token",
    "patient": "reference",
    "achievement-status": "token",
    "category": "token",
    "lifecycle-status": "token",
    "start-date": "date",
    "subject": "reference",
    "target-date": "date",
}

goal_references = {
    "patient": ["Patient"],
    "subject": ["Group", "Organization", "Patient"],
}
