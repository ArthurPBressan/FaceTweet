# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template, url_for, redirect, request
from flask.ext.security import login_required, current_user

from sisgep1.base import db
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
    if fb_user_connection:
        if not fb_user_connection.cover_url:
            cover_node = fb.get_connections(id=fb_user_connection.provider_user_id,
                                            connection_name='',
                                            fields='cover').get('cover')
            if cover_node:
                fb_user_connection.cover_url = cover_node['source']
                fb_user_connection.cover_x = cover_node.get('offset_x', 0)
                fb_user_connection.cover_y = cover_node.get('offset_y', 0)
                db.session.commit()
        args = {
            'fields': ['message', 'story', 'picture', 'link'],
        }
        fb_posts = fb.get_connections(id=fb_user_connection.provider_user_id,
                                      connection_name='posts', **args)['data']
    return render_template('feed.html', fb_posts=fb_posts,
                           fb_connection=fb_user_connection)


@bp.route('/facebook/post/', methods=['POST'])
@login_required
def post_facebook():
    fb = social.facebook.get_api()
    fb_user_connection = current_user.get_connection('facebook')
    import ipdb;ipdb.set_trace();
    return redirect(url_for('.index'))
    pass

@bp.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection())
