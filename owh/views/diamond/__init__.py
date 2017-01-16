# -*- coding: utf-8 -*-
# owh (c) Thomas C Hicks

import flask

diamond_blueprint = flask.Blueprint(
    'diamond_blueprint',
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='/static/diamond',
)
