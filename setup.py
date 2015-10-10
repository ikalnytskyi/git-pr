#!/usr/bin/env python
# coding: utf-8

import os

from io import open
from setuptools import setup, find_packages

from git_pr import __version__ as version
from git_pr import __license__ as license


here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

manpage = os.path.join(here, 'man', 'git-pr.1')
mansection = os.path.basename(manpage).split('.')[1]


setup(
    name='git-pr',
    version=version,

    description="Tool to fetch GitHub's pull requests",
    long_description=long_description,
    license=license,
    url='http://github.com/ikalnitsky/git-pr/',
    keywords='git github pull-request',

    author='Igor Kalnitsky',
    author_email='igor@kalnitsky.org',

    packages=find_packages(exclude=['tests*']),
    test_suite='tests',

    entry_points={
        'console_scripts': [
            'git-pr = git_pr.__main__:main',
        ],
    },

    data_files=[
        (os.path.join('share', 'man', 'man' + mansection), [manpage]),
    ],

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',

        'Topic :: Terminals',
        'Topic :: Software Development',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
