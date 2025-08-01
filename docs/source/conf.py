# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Hosting Documentation'
copyright = '2025, CSE @ PSTU'
author = 'Mir Suhail Asarat'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'myst_parser',
]

source_suffix = ['.rst', '.md']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
  'flyout_display': 'attached',  # or 'hidden' to disable default injected flyout
  'version_selector': True,
  'language_selector': True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
