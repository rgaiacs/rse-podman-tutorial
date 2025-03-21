# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

host = os.getenv("CI_SERVER_HOST", "readthedocs.org")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Podman Desktop Tutorial'
copyright = '2025, Raniere Gaia Costa da Silva'
author = 'Raniere Gaia Costa da Silva'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

if host == "git.gesis.org":
    html_theme = "sphinx_rtd_theme"  # Documentation at https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html

    html_baseurl = '/podman/learn/podman-desktop/'

    html_context = {
        "display_gitlab": True,
        "gitlab_host": "git.gesis.org",
        "gitlab_user": "rse",
        "gitlab_repo": "podman/learn/podman-desktop",
        "gitlab_version": "main",
        "conf_py_path": "/source/",
    }
elif host == "readthedocs.org":
    html_theme = "sphinx_rtd_theme"  # Documentation at https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html

    html_baseurl = ''

    html_context = {
        "display_github": True,
        "github_user": "rgaiacs",
        "github_repo": "rse-podman-tutorial",
        "github_version": "main",
        "conf_py_path": "/source/",
    }

html_copy_source = False

html_theme_options = {
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": True,
    "vcs_pageview_mode": "blob",
}

html_static_path = ["_static"]
