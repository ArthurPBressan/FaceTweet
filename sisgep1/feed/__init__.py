# coding: UTF-8
from __future__ import absolute_import

from sisgep1.feed import rotas, models


def init_app(app):
    rotas.init_app(app)
    models.init_app(app)
