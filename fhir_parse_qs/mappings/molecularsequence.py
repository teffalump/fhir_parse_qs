__all__ = ["molecularsequence_mapping", "molecularsequence_references"]

molecularsequence_mapping = {
    "chromosome": "token",
    "identifier": "token",
    "patient": "reference",
    "referenceseqid": "token",
    "type": "token",
    "variant-end": "number",
    "variant-start": "number",
    "window-end": "number",
    "window-start": "number",
    "chromosome-variant-coordinate": "composite",
    "chromosome-window-coordinate": "composite",
    "referenceseqid-variant-coordinate": "composite",
    "referenceseqid-window-coordinate": "composite",
}

molecularsequence_references = {
    "patient": ["Patient"],
}
