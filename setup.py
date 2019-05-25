# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
import sys

from setuptools import setup, find_packages

here = os.path.dirname(os.path.abspath(__file__))

version_ns = {}
with open(os.path.join(here, 'jupyterlab_pygments', '_version.py')) as f:
    exec(f.read(), {}, version_ns)

setup_args = {
    'name': 'jupyterlab_pygments',
    'version': version_ns['__version__'],
    'description': 'Pygments theme using JupyterLab CSS variables',
    'packages': find_packages(),
    'zip_safe': False,
    'install_requires': [
        'pygments>=2.4.1,<3'
    ],
    'author': 'Jupyter Development Team',
    'author_email': 'jupyter@googlegroups.com',
    'url': 'http://jupyter.org',
    'keywords': [
        'jupyterlab',
        'pygments'
    ]
}

setup(**setup_args)

