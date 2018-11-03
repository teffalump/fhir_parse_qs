import json
from urllib.request import urlretrieve
from zipfile import ZipFile
import os

BASE_URL='http://www.hl7.org/fhir/definitions.json.zip'
JSON_FILE='search-parameters.json'

def download_specifications(url=BASE_URL):
    local_file, _ = urlretrieve(url)
    with ZipFile(local_file) as z:
        z.extract(JSON_FILE)

def get_imported_json(target=JSON_FILE):
    with open(target) as json_file:
        params = json.load(json_file)
    return params

def get_data(data):
    parsed = []
    for entry in data['entry']:
        if entry['resource']['id'] == 'clinical-encounter':
            entry['resource']['target'] = ['Encounter']
        if entry['resource']['id'] == 'clinical-patient':
            entry['resource']['target'] = ['Patient']
        if entry['resource']['base'][0] in ('Resource', 'DomainResource'):
            entry['resource']['base'][0] = 'common'
        parsed.append({
                'resource': entry['resource']['base'],
                'name': entry['resource']['name'],
                'type':  entry['resource']['type'],
                'targets': entry['resource'].get('target'),
                    })
    return parsed

def organize(entries):
    organized = {}
    for entry in entries:
        r = entry.pop('resource')
        for b in r:
            try:
                organized[b].append(entry)
            except KeyError:
                organized[b] = [entry]
    organized['control'] = [{'name': '_sort', 'type': 'string', 'targets': None},
                            {'name': '_count', 'type': 'number', 'targets': None},
                            {'name': '_include', 'type': 'string', 'targets': None},
                            {'name': '_revinclude', 'type': 'string', 'targets': None},
                            {'name': '_summary', 'type': 'string', 'targets': None},
                            {'name': '_containded', 'type': 'string', 'targets': None},
                            {'name': '_containedType', 'type': 'string', 'targets': None},
                            ]
    return organized

def write_mappings(data):
    for key,value in data.items():
        #write each resource
        with open(key.lower()+'.py', 'w') as f:
            f.write('__all__=[\'{}_mapping\', \'{}_references\']\n\n'.format(key.lower(), key.lower()))
            f.write('{}_mapping = {{\n'.format(key.lower()))
            for p in value:
                f.write('    \'{}\': \'{}\',\n'.format(p['name'], p['type']))
            f.write('    }\n\n')
            f.write('{}_references = {{\n'.format(key.lower()))
            for p in value:
                if p['targets']:
                    f.write('    \'{}\': [ {} ],\n'.format(p['name'], ', '.join(["'" + x + "'" for x in p['targets']])))
            f.write('    }\n')

def write_init(data):
    with open('__init__.py', 'w') as f:
        f.write('__all__=[\'search_types\', \'search_references\']\n\n')
        for resource in sorted(data):
            f.write('from .{} import {}, {}\n'.format(resource.lower(), resource.lower()+'_mapping', resource.lower()+'_references'))
        f.write('\n')
        f.write('search_types = {\n')
        for resource in sorted(data):
            f.write('    \'{}\': {},\n'.format(resource, resource.lower()+'_mapping'))
        f.write('    }\n\n')
        f.write('search_references = {\n')
        for resource in sorted(data):
            f.write('    \'{}\': {},\n'.format(resource, resource.lower()+'_references'))
        f.write('    }')

def cleanup():
    os.remove(JSON_FILE)

if __name__=='__main__':
    download_specifications()
    d = organize(get_data(get_imported_json()))
    write_mappings(d)
    write_init(d)
    cleanup()
