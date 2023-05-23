# -*- coding: utf-8 -*-
# flake8: noqa (hacky way of sharing config, etc...)

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

authors = u'NOAA-EMC, NASA-GMAO'
copyright = u'2023 ' + authors
description = 'Short description for html meta description.'
version = release = '0.0.1'

html_static_path += ['_static']
templates_path = ['_templates']

html_css_files = [
    'nbsite.css',
    'custom.css'
]

extensions += [
    'sphinx_copybutton'
]

html_theme = 'sphinx_holoviz_theme'
# logo file etc should be in html_static_path, e.g. _static
# only change colors in primary, primary_dark, and secondary
html_theme_options = {
    'custom_css': 'site.css',
    'primary_color': 'MediumSeaGreen',
    'primary_color_dark': 'sienna',
    'secondary_color': 'DarkTurquoise',
}
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo.png"

myst_enable_extensions = ["colon_fence"]

html_context.update({
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'VERSION': version,
})
