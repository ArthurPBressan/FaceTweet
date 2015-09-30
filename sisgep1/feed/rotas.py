# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask.ext.security import login_required, current_user

from sisgep1.base import db
from sisgep1.feed.models import social, User

bp = Blueprint('feed', __name__, static_folder='static', template_folder='templates')


def init_app(app):
    app.register_blueprint(bp, url_prefix='/feed')


@bp.route('/')
@bp.route('/<user_email>')
@login_required
def index(user_email=None):
    if not user_email:
        return redirect(url_for('.index', user_email=current_user.email))
    user = User.query.filter_by(email=user_email).first_or_404()
    same_user = user == current_user
    fb = social.facebook.get_api()
    fb_user_connection = user.get_connection('facebook')
    posts = []
    if fb_user_connection:
        if not fb_user_connection.cover_url and same_user:
            cover_node = fb.get_object(id=fb_user_connection.provider_user_id,
                                       fields='cover').get('cover')
            if cover_node:
                fb_user_connection.cover_url = cover_node['source']
                fb_user_connection.cover_x = cover_node.get('offset_x', 0)
                fb_user_connection.cover_y = cover_node.get('offset_y', 0)
                db.session.commit()
        args = {
            'fields': ['message', 'story', 'picture', 'link'],
        }
        posts = fb.get_connections(id=fb_user_connection.provider_user_id,
                                   connection_name='posts', **args)['data']
    twitter = social.twitter.get_api()
    twitter_user_connection = user.get_connection('twitter')
    tweets = []
    if twitter_user_connection:
        tweets = twitter.GetUserTimeline()
    return render_template('feed.html', posts=posts, tweets=tweets,
                           facebook=fb_user_connection, same_user=same_user,
                           twitter=twitter_user_connection, user=user)


@bp.route('/facebook/post/', methods=['POST'])
@login_required
def post_facebook():
    fb = social.facebook.get_api()
    fb_user_connection = current_user.get_connection('facebook')
    message = request.form['message'].encode('utf-8')
    fb.put_object(parent_object=fb_user_connection.provider_user_id,
                  connection_name='feed', message=message)
    return redirect(url_for('.index'))


@bp.route('/twitter/post/', methods=['POST'])
@login_required
def post_twitter():
    message = request.form['message']
    if len(message) > 140:
        flash('Status is over 140 characters.', 'danger')
    else:
        twitter = social.twitter.get_api()
        twitter.PostUpdate(message)
    return redirect(url_for('.index'))


@bp.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection())
