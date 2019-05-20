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
    'description': 'Pygments theme',
    'packages': find_packages(),
    'zip_safe': False,
    'install_requires': [
        'pygments>=2.4.1,<3'
    ],
    'author': 'QuantStack',
    'author_email': 'info@quantstack.net',
    'keywords': [
        'jupyterlab',
        'pygments'
    ]
}

setup(**setup_args)

