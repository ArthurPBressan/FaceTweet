# coding: UTF-8
from __future__ import absolute_import

from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import Integer, String, Boolean, DateTime

from sisgep1.base import db, JSONSerializationMixin

security = Security()


def init_app(app):
    usuario_datastore = SQLAlchemyUserDatastore(db, Usuario, Role)
    security.init_app(app, db, usuario_datastore)

    @app.before_first_request
    def create_user():
        usuario_datastore.create_user(email='admin@admin', senha='admin')
        db.session.commit()

roles_users = db.Table('roles_usuarios',
                       Column('usuario_id', Integer(), ForeignKey('usuario.id')),
                       Column('role_id', Integer(), ForeignKey('role.id')))


class Role(db.Model, RoleMixin, JSONSerializationMixin):
    ignored_fields = ['usuarios']

    id = Column(Integer(), primary_key=True)
    nome = Column(String(80), unique=True)
    descricao = Column(String(255))


class Usuario(db.Model, UserMixin, JSONSerializationMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    senha = Column(String(255))
    ativo = Column(Boolean())
    confirmado = Column(DateTime())
    roles = relationship('Role', secondary=roles_users,
                         backref=backref('usuarios', lazy='dynamic'))
