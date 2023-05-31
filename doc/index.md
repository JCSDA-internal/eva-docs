---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  name: python3
---

# Eva - Evaluation and Verification of the Analysis

```{image} ./_static/images/eva_logo_ball.png
---
alt: eva logo
align: center
width: 35%
---
```

Eva is a collaborative project to provide diagnostics that can be used to assess the performance of
a JEDI-based data assimilation system.

Eva is designed with a completely flexible API that allows diagnostics to be run in a standalone
mode, within a workflow system and through, for example, Jupyter notebooks. There are several entry
points, depending on what the user is interested in looking at. The following documentation explains
how to use Eva and contribute new diagnostics.

```{toctree}
:titlesonly:
:hidden:
:maxdepth: 2

Home <self>
Getting Started <getting_started/index>
Eva Infrastructure <eva_infrastructure/index>
Diagnostics <diagnostics/index>
Plot Tools <plot_tools/index>
Eva Example <eva_example>
```
