# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template
from flask.ext.security import login_required, current_user

from sisgep1.feed.models import social

bp = Blueprint('feed', __name__, static_folder='static', template_folder='templates')


def init_app(app):
    app.register_blueprint(bp, url_prefix='/feed')


@bp.route('/')
@login_required
def index():
    fb = social.facebook.get_api()
    fb_user_connection = current_user.get_connection('facebook')
    fb_posts = []
    print fb_user_connection
    if fb_user_connection:
        fb_posts = fb.get_connections(id=fb_user_connection.provider_user_id, connection_name='posts')['data']
        print fb_user_connection.provider_user_id
        print fb_posts
    return render_template('feed.html', fb_posts=fb_posts)


@bp.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection())
