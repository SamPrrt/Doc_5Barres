project = "AaPsRt_info_indus_tutorial"
copyright = "2026, Amine ALAOUI, Samuel PERROT, Thomas ROUX"
author = "Amine ALAOUI, Samuel PERROT, Thomas ROUX"
release = "1.0"

extensions = [
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinx_design",
]
myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
language = "fr"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = [".rst", ".md"]

html_theme = "sphinx_rtd_theme"
html_sidebars = {"**": ["globaltoc.html", "relations.html", "searchbox.html"]}

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

rst_prolog = """
.. role:: text-bold-black-on-red
   :class: text-bold-black-on-red

.. |br| raw:: html

        <br>
"""