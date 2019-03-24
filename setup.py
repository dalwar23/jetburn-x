#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for jetburn

Install jetburn with:
python2/3 setup.py install
"""

# Source code meta data
__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'

# Import python libraries
import os
import sys
from setuptools import setup, find_packages


# Check if enough parameter has been given to install or not
if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")


# Check python version before installing
if sys.version_info[:2] < (2, 7):
    print("JETBURN requires Python 2.7 or later (%d.%d detected)." % sys.version_info[:2])
    sys.exit(-1)


# Get version and release for this package
package_name = 'jetburn'
release_file = os.path.join(package_name, '_version.py')
release_info = {}
with open(release_file, 'rb') as rf:
    exec(rf.read(), release_info)


# Read the README.md file for long description
def readme():
    with open('README.rst') as f:
        return f.read()


# Standard boilerplate to run this script
if __name__ == "__main__":
    setup(
        name=package_name,
        version=release_info['__full_version__'],
        maintainer='Dalwar Hossain',
        maintainer_email='dalwar.hossain@protonmail.com',
        author=release_info['__author__'],
        author_email=release_info['__author_email__'],
        description='jetburn - Airline ticket explorer program',
        keywords=['jetburn', 'airlines', 'tickets', 'fares'],
        long_description=readme(),
        license=release_info['__app_license__'],
        platforms=['Linux', 'Mac OSX', 'Windows', 'Unix'],
        url='https://github.com/dharif23/jetburn',
        download_url='https://github.com/dharif23/jetburn',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development :: Libraries :: Python Modules'],
        packages=find_packages(),
        entry_points={
            'console_scripts': ['jetburn=jetburn.flight_control:jetburn_cli',
                                'jetburn-info=jetburn.flight_control:jetburn_info'
                                ],
        },
        include_package_data=True,
        install_requires=['pyrainbowterm',
                          'pyfiglet',
                          'wasabi',
                          'PyInquirer',
                          'tabulate',
                          'datapackage',
                          'requests',
                          'sphinx',
                          'recommonmark',
                          'sphinx_rtd_theme',
                          ],
        test_suite='nose.collector',
        tests_require=['nose', 'nose-cover3'],
        zip_safe=False,
    )
