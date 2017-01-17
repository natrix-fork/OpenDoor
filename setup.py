#! /usr/bin/env python

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

from setuptools import setup, find_packages
import pypandoc
import glob
from src import Controller

try:
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='opendoor',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html

    version=Controller.local_version(),

    description='OWASP Directory Access scanner',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/stanislav-web/OpenDoor',

    # Author details
    author='Stanislav WEB',
    author_email='stanisov@gmail.com',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Choose your license
    license='GPL',
    test_suite='tests',

    # What does your project relate to?
    keywords=['owasp scanner', 'directory scanner', 'access directory scanner', 'web spider', 'auth scanner', 'dir search'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'opendoor=opendoor:main',
            'coveralls = coveralls.cli:main',
        ],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('data', glob.glob("/data/*.dat"))],

    scripts=['opendoor.py'],
    install_requires=[line.rstrip('\n') for line in open('requirements.txt')],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',

        # Specify the additional categories
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking'
        'Topic :: Software Development :: src :: Python Modules',
    ],
)
