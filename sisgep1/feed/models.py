# coding: UTF-8
from __future__ import absolute_import

from sisgep1.base import db, JSONSerializationMixin

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String


def init_app(app):
    pass


class Usuario(db.Model, JSONSerializationMixin):

    id = Column(Integer, primary_key=True)
