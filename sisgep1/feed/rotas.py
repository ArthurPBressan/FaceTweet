# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template, current_app

bp = Blueprint('feed', __name__, static_folder='static', template_folder='templates')


def init_app(app):
    app.register_blueprint(bp, url_prefix='/feed')


@bp.route('/')
def index():
    fb = current_app.extensions['facebook']
    fb_posts = fb.get_connections(id='me', connection_name='posts')['data']
    print fb_posts[0]
    return render_template('feed.html', fb_posts=fb_posts)
