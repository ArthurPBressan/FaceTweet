# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template
from flask.ext.security import login_required

from sisgep1.feed.models import social

bp = Blueprint('feed', __name__, static_folder='static', template_folder='templates')


def init_app(app):
    app.register_blueprint(bp, url_prefix='/feed')


@bp.route('/')
@login_required
def index():
    return render_template('feed.html')


@bp.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection())
