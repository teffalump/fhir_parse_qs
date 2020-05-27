import json
from urllib.request import urlretrieve
import os

BASE_URL = "http://www.hl7.org/fhir/search-parameters.json"
JSON_FILE = "search-parameters.json"
TARGET_DIR = "mappings/"


def setup():
    try:
        os.mkdir(TARGET_DIR)
        print("Created target directory.")
    except:
        print("Target directory already exists, skipping creation.")


def download_specifications(url=BASE_URL):
    urlretrieve(url, filename=JSON_FILE)
    print("Downloaded specifications.")


def get_imported_json(target=JSON_FILE):
    params = {}
    with open(target) as json_file:
        params = json.load(json_file)
    return params


def get_data(data):
    parsed = []
    for entry in data["entry"]:
        if entry["resource"]["id"] == "clinical-encounter":
            entry["resource"]["target"] = ["Encounter"]
        if entry["resource"]["id"] == "clinical-patient":
            entry["resource"]["target"] = ["Patient"]
        if entry["resource"]["base"][0] in ("Resource", "DomainResource"):
            entry["resource"]["base"][0] = "common"
        parsed.append(
            {
                "resource": entry["resource"]["base"],
                "name": entry["resource"]["name"],
                "type": entry["resource"]["type"],
                "targets": entry["resource"].get("target"),
            }
        )
    return parsed


def organize(entries):
    organized = {}
    for entry in entries:
        r = entry.pop("resource")
        for b in r:
            try:
                organized[b].append(entry)
            except KeyError:
                organized[b] = [entry]
    organized["control"] = [
        {"name": "_sort", "type": "string", "targets": None},
        {"name": "_count", "type": "number", "targets": None},
        {"name": "_include", "type": "string", "targets": None},
        {"name": "_revinclude", "type": "string", "targets": None},
        {"name": "_summary", "type": "string", "targets": None},
        {"name": "_total", "type": "number", "targets": None},
        {"name": "_elements", "type": "string", "targets": None},
        {"name": "_contained", "type": "string", "targets": None},
        {"name": "_containedType", "type": "string", "targets": None},
    ]
    return organized


def write_mappings(data):
    for key, value in data.items():
        filename = os.path.join(TARGET_DIR, key.lower() + ".py")
        # write each resource
        with open(filename, "w") as f:
            f.write(
                "__all__=['{}_mapping', '{}_references']\n\n".format(
                    key.lower(), key.lower()
                )
            )
            f.write("{}_mapping = {{\n".format(key.lower()))
            for p in value:
                f.write("    '{}': '{}',\n".format(p["name"], p["type"]))
            f.write("    }\n\n")
            f.write("{}_references = {{\n".format(key.lower()))
            for p in value:
                if p["targets"]:
                    f.write(
                        "    '{}': [ {} ],\n".format(
                            p["name"], ", ".join(["'" + x + "'" for x in p["targets"]])
                        )
                    )
            f.write("    }\n")
    print("Generated mappings.")


def write_init(data):
    filename = os.path.join(TARGET_DIR, "__init__.py")
    with open(filename, "w") as f:
        f.write("__all__=['search_types', 'search_references']\n\n")
        for resource in sorted(data):
            f.write(
                f"from .{resource.lower()} import {resource.lower()}_mapping, {resource.lower()}_references\n"
            )
        f.write("\nsearch_types = {\n")
        for resource in sorted(data):
            f.write(f"    '{resource}': {resource.lower()}_mapping,\n")
        f.write("    }\n\n")
        f.write("search_references = {\n")
        for resource in sorted(data):
            f.write(f"    '{resource}': {resource.lower()}_references,\n")
        f.write("    }")
    print("Generated init file.")


def cleanup():
    os.remove(JSON_FILE)


if __name__ == "__main__":
    setup()
    download_specifications()
    d = organize(get_data(get_imported_json()))
    write_mappings(d)
    write_init(d)
    cleanup()
