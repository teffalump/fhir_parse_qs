__all__ = ["device_mapping", "device_references"]

device_mapping = {
    "device-name": "string",
    "identifier": "token",
    "location": "reference",
    "manufacturer": "string",
    "model": "string",
    "organization": "reference",
    "patient": "reference",
    "status": "token",
    "type": "token",
    "udi-carrier": "string",
    "udi-di": "string",
    "url": "uri",
}

device_references = {
    "location": ["Location"],
    "organization": ["Organization"],
    "patient": ["Patient"],
}
