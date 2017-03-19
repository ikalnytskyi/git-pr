#!/usr/bin/env python
# coding: utf-8

import os

from io import open
from setuptools import setup, find_packages


here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

manpage = os.path.join(here, 'man', 'git-pr.1')
mansection = os.path.basename(manpage).split('.')[1]


setup(
    name='git-pr',
    description='Tool to fetch GitHub pull requests.',
    long_description=long_description,
    license='MIT',
    url='http://github.com/ikalnytskyi/git-pr/',
    keywords='git github pull-request',
    author='Ihor Kalnytskyi',
    author_email='ihor@kalnytskyi.com',
    packages=find_packages(exclude=['docs', 'tests*']),
    test_suite='tests',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm >= 1.15',
    ],
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
