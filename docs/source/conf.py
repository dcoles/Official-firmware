# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TinyWATCH S3'
copyright = '2024, UnexpectedMaker'
author = 'UnexpectedMaker'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'breathe']

templates_path = ['_templates']
exclude_patterns = []

# -- Breathe configuration ---------------------------------------------------
# https://breathe.readthedocs.io/en/latest/quickstart.html

breathe_projects_source = {
    'tinywatch-s3': ('../../Platform-io-source/src', [
        'activity.h',
        'display.h',
        'tinywatch.h',
    ]),
}
breathe_default_project = 'tinywatch-s3'
breathe_domain_by_extension = {
    "h" : "cpp",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
