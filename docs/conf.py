# -*- coding: utf-8 -*-
"""
    Sphinx configuration file for building git-pr's documentation.
"""

from __future__ import unicode_literals

import re
import os
import sys

import pkg_resources


# project settings
project = 'git-pr'
copyright = '2015, Ihor Kalnytskyi'
release = pkg_resources.get_distribution('git-pr').version
version = re.sub('[^0-9.]', '', release)

# sphinx settings
extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

# apply RTD theme only if we aren't on rtd
if not os.environ.get('READTHEDOCS', None) == 'True':
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
