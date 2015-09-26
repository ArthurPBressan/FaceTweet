# coding: UTF-8
from __future__ import absolute_import

from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Integer, String, Boolean, DateTime

from sisgep1.base import db, JSONSerializationMixin

security = Security()
social = Social()


def init_app(app):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    @app.before_first_request
    def create_user():
        if not User.query.filter_by(email='admin@admin').first():
            user_datastore.create_user(email='admin@admin', password='admin')
            db.session.commit()

    social.init_app(app, SQLAlchemyConnectionDatastore(db, Connection))


roles_users = db.Table('roles_users',
                       Column('user_id', Integer(), ForeignKey('user.id')),
                       Column('role_id', Integer(), ForeignKey('role.id')))


class Role(db.Model, RoleMixin, JSONSerializationMixin):
    ignored_fields = ['users']

    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class User(db.Model, UserMixin, JSONSerializationMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary=roles_users,
                         backref=backref('users', lazy='dynamic'))


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)
