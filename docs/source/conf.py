# Configuration file for the Sphinx documentation builder.
# -- Project information

project = 'NRGSuite-Qt'
copyright = '2024, DesCoteaux, Galdino, Teruel and Najmanovich'
author = 'DesCoteaux, Galdino, Teruel and Najmanovich'

release = '0.1'
version = '2025.14.4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    'sphinx_new_tab_link'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "_static/images/main_menu/logo.png"

# -- Options for EPUB output
epub_show_urls = 'footnote'
html_theme_options = {'logo_only': True}

def setup(app):
    app.add_css_file('css/my_theme.css')

html_static_path = ['_static']