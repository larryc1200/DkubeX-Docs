# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from distutils.version import LooseVersion

#from recommonmark.transform import AutoStructify

import sphinx_material

#FORCE_CLASSIC = os.environ.get("SPHINX_MATERIAL_FORCE_CLASSIC", False)
#FORCE_CLASSIC = FORCE_CLASSIC in ("1", "true")

# -- Project information -----------------------------------------------------

project = u'<DKubeX>'
copyright = u'2023, One Convergence, Inc.  All rights reserved'
author = u'<OneConvergence>'

html_show_sphinx = False

# The short X.Y version
version = u'R0.1'
# The full version, including alpha/beta/rc tags
release = u'R0.1'
# Jun-2023

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    'sphinx_tabs.tabs',
    'sphinx.ext.extlinks',
    'linuxdoc.rstFlatTable',
]

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["._templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["./_static"]

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
# html_theme_path = sphinx_material.html_theme_path()
html_theme = "sphinx_material"

html_context = {
    'css_files': [
        '_static/css/custom.css']
     }

# material theme options (see theme.conf for more information)
html_theme_options = {
    "globaltoc_depth": 2,
    "master_doc": False,
    "nav_title": "DKubeX User Guide",
    "table_classes": ["left-align-right-col", "center-align-2nd-col", "double-border", "left-align-left-col", "left-align-right-col", "no-border", "with-border"]
}

html_logo = "images/logo.png"

#if FORCE_CLASSIC:
#    print("!!!!!!!!! Forcing classic !!!!!!!!!!!")
#    html_theme = "classic"
#    html_theme_options = {}
#    html_sidebars = {"**": ["globaltoc.html", "localtoc.html", "searchbox.html"]}

language = "en"
#html_last_updated_fmt = ""

todo_include_todos = True
#html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

# External Link Base Text
# extlinks = {'install': ('../../install/install3_x/%s', '')
# }

# Open external links in new tab
from sphinx.writers.html import HTMLTranslator
class PatchedHTMLTranslator(HTMLTranslator):
    def visit_reference(self, node):
        if node.get('newtab') or not (node.get('target') or node.get('internal') or 'refuri' not in node):
            node['target'] = '_blank'
        super().visit_reference(node)

def setup(app):
    app.set_translator('html', PatchedHTMLTranslator)