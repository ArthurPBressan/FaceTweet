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
    social.init_app(app, SQLAlchemyConnectionDatastore(db, Connection))


roles_users = db.Table('roles_users',
                       Column('user_id', Integer(), ForeignKey('user.id')),
                       Column('role_id', Integer(), ForeignKey('role.id')))

followers = db.Table('followers',
                     Column('follower_id', Integer(), ForeignKey('user.id')),
                     Column('followed_id', Integer(), ForeignKey('user.id')))


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
    connections = relationship('Connection', backref='user')

    followed = relationship('User',
                            secondary=followers,
                            primaryjoin=(followers.c.follower_id == id),
                            secondaryjoin=(followers.c.followed_id == id),
                            backref=backref('followers', lazy='dynamic'),
                            lazy='dynamic')

    def get_connection(self, name):
        for connection in self.connections:
            if connection.provider_id == name:
                return connection

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0


class Connection(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    provider_id = Column(String(255))
    provider_user_id = Column(String(255))
    access_token = Column(String(255))
    secret = Column(String(255))
    display_name = Column(String(255))
    profile_url = Column(String(512))
    image_url = Column(String(512))
    rank = Column(Integer)

    full_name = Column(String(255))
    email = Column(String(255))

    cover_url = Column(String(512))
    cover_x = Column(Integer)
    cover_y = Column(Integer)
