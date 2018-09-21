import sys
import os
from shutil import rmtree
from setuptools import setup, Command

NAME = 'fhir_parse_qs'

# Convert MD to RST
try:
    from pypandoc import convert_file
    read_md = lambda f: convert_file(f, 'rst')
except ModuleNotFoundError:
    print('warning: pypandoc module not found, cannot covert Markdown to RST')
    read_md = open(f, 'r').read()

# Copy from kennethreitz/setup.py
here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass
        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

setup(name = 'fhir_parse_qs',
        version = about['__version__'],
        description = 'Parse FHIR query string',
        long_description = read_md(os.path.join(here, 'README.md')),
        url = 'https://github.com/teffalump/fhir_parse_qs',
        author = 'teffalump',
        author_email = 'chris@teffalump.com',
        packages = ['fhir_parse_qs'],
        install_requires = ['pendulum'],
        include_package_data = True,
        zip_safe = False,
        classifiers = ['Development Status :: 2 - Pre-Alpha',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                       'Operating System :: OS Independent'],
        cmdclass={
            'upload': UploadCommand,
            },
        )
