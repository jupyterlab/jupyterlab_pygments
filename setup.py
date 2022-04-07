"""
jupyterlab_pygments setup
"""
import json
from pathlib import Path
from os.path import join as pjoin

from jupyter_packaging import (
    wrap_installers,
    npm_builder,
    get_data_files,
    get_version
)

import setuptools

HERE = Path(__file__).parent.resolve()

# Get the package info from package.json
pkg_json = json.loads((HERE / "package.json").read_bytes())

# The name of the project
name = "jupyterlab_pygments"

lab_path = (HERE / pkg_json["jupyterlab"]["outputDir"])

# Representative files that should exist after a successful build
ensured_targets = [
    str(lab_path / "package.json"),
    str(lab_path / "static/style.js")
]

labext_name = pkg_json["name"]

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path.relative_to(HERE)), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str("."), "install.json"),
]

long_description = (HERE / "README.md").read_text()

post_develop = npm_builder(
    build_cmd="install:extension", source_dir="src", build_dir=lab_path,
    npm=['jlpm']
)

setup_args = dict(
    version=get_version(pjoin(name, '_version.py')),
    cmdclass=wrap_installers(
        post_develop=post_develop, ensured_targets=ensured_targets
    ),
    data_files=get_data_files(data_files_spec)
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
