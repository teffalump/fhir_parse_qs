import os
from setuptools import setup

NAME = 'fhir_parse_qs'

with open('README.md') as readme:
    README = readme.read()
    README_TYPE = "text/markdown"

with open(os.path.join(NAME, 'VERSION')) as version:
    VERSION = version.readlines()[0].strip()

with open('requirements.txt') as requirements:
    REQUIREMENTS = [line.rstrip() for line in requirements if line != '\n']

setup(name = 'fhir_parse_qs',
        version = VERSION,
        description = 'Parse FHIR query strings',
        long_description = README,
        long_description_content_type = README_TYPE,
        url = 'https://github.com/teffalump/fhir_parse_qs',
        author = 'teffalump',
        author_email = 'chris@teffalump.com',
        packages = ['fhir_parse_qs'],
        install_requires = REQUIREMENTS,
        include_package_data = True,
        zip_safe = False,
        classifiers = ['Development Status :: 2 - Pre-Alpha',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                       'Operating System :: OS Independent'],
        )
