# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint

bp = Blueprint('feed', __name__, static_folder='static', template_folder='templates')


def init_app(app):
    app.register_blueprint(bp, url_prefix='/feed')


@bp.route('/')
def index():
    return 'index'
