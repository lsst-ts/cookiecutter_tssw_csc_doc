"""Sphinx configuration file for TSSW package"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.ts.{{cookiecutter.csc_name}}


_g = globals()
_g.update(build_package_configs(
    project_name='{{cookiecutter.csc_repo_name}}',
    version=lsst.ts.{{cookiecutter.csc_name}}.version.__version__
))
