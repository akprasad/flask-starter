# -*- coding: utf-8 -*-
"""
    starter.views
    ~~~~~~~~~~~~~

    Basic views

    :license: MIT and BSD
"""

from flask import render_template
from starter import app


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('errors/500.html'), 500
