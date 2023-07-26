# -*- coding: utf-8 -*-
# flake8: noqa (hacky way of sharing config, etc...)

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

project = u''
copyright = u''

extensions += [
    'sphinx_copybutton'
]

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
