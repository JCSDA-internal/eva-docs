# -*- coding: utf-8 -*-
# flake8: noqa (hacky way of sharing config, etc...)

from nbsite.shared_conf import *
import os
import sys
###################################################
# edit things below as appropriate for your project
sys.path.insert(0, os.path.abspath('eva/src/'))

project = u''
copyright = u''

extensions += [
    'sphinx_copybutton',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
]

autoclass_content = 'both'

html_show_sourcelink = False
html_theme = "pydata_sphinx_theme"
html_favicon = "_static/favicon.ico"
html_logo = "_static/images/eva_logo_ball.png"

html_theme_options = {
    "footer_items": [
        "copyright",
        "last-updated",
    ]
}

myst_enable_extensions = ["colon_fence"]
