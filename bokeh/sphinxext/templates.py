from __future__ import absolute_import

from jinja2 import Environment, PackageLoader

_env = Environment(loader=PackageLoader('bokeh.sphinxext', '_templates'))

CCB_PROLOGUE = _env.get_template("collapsible_code_block_prologue.html")
CCB_EPILOGUE = _env.get_template("collapsible_code_block_epilogue.html")

GALLERY_DETAIL = _env.get_template("gallery_detail.rst")
GALLERY_PAGE = _env.get_template("gallery_page.rst")

JINJA_DETAIL = _env.get_template("jinja_detail.rst")

MODEL_DETAIL = _env.get_template("model_detail.rst")

PALETTE_DETAIL = _env.get_template("palette_detail.html")

PLOT_SOURCE = _env.get_template("plot_source.rst")

PROP_DETAIL = _env.get_template("prop_detail.rst")
