__all__ = ["testreport_mapping", "testreport_references"]

testreport_mapping = {
    "identifier": "token",
    "issued": "date",
    "participant": "uri",
    "result": "token",
    "tester": "string",
    "testscript": "reference",
}

testreport_references = {
    "testscript": ["TestScript"],
}
