# Configuration file for the Sphinx documentation builder.
from docutils import nodes, parsers
from docutils.parsers.rst import roles
# -- Project information

project = 'NRGSuite-Qt'
copyright = '2024, DesCoteaux, Galdino, Teruel and Najmanovich'
author = 'DesCoteaux, Galdino, Teruel and Najmanovich'

release = '0.1'
version = '1.0'

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

def underline_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.inline(rawtext, text, classes=['underline'])], []

roles.register_local_role('underline', underline_role)


def setup(app):
    app.add_css_file('css/my_theme.css')

html_static_path = ['_static']