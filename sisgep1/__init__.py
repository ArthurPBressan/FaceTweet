# coding: UTF-8
from __future__ import absolute_import

from flask import Flask, redirect, url_for

from sisgep1 import base


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('settings')
    app.config.from_pyfile('settings_local.py', silent=True)

    base.init_app(app)

    @app.route('/')
    def index():
        return redirect(url_for('feed.index'))

    return app
