"""Sphinx configuration file for TSSW package"""

from documenteer.conf.pipelinespkg import *


project = "{{cookiecutter.csc_repo_name}}"
html_theme_options["logotext"] = project
html_title = project
html_short_title = project

intersphinx_mapping["ts_xml"] = ("https://ts-xml.lsst.io", None)
