#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
#
# ------------------------------------------------

# imports
# -------
import os

# config
# ------
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# requirements
# ------------
with open('requirements.txt') as f:
    REQUIREMENTS = f.read().strip().split('\n')

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-runner'
]

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'Non-Covalent Molecular Interaction Rules'

# exec
# ----
setup(
    name="molecular_interaction_rules",
    version="0.2",
    packages=['molecular_interaction_rules'],
    license='GPL',
    author="Suliman Sharif",
    author_email="sharifsuliman1@gmail.com",
    url="https://www.github.com/mackerell-lab/Non-Covalent-Molecular-Interaction-Rules",
    install_requires=REQUIREMENTS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    keywords='molcules non-covalent interactions rules geometry',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
