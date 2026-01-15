# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Night Owl Protect'
copyright = '2024, Night Owl Security'
author = 'Night Owl Security Team'
release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx_copybutton',
]

# Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The master toctree document.
master_doc = 'index'

# Language settings
language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Custom CSS
html_css_files = [
    'css/custom.css',
]

# Logo
# html_logo = '_static/logo.png'

# Favicon
# html_favicon = '_static/favicon.ico'

# -- Options for PDF output --------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
}

# -- Options for EPUB output -------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# -- MyST Parser Options -----------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]
