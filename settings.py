# coding: UTF-8
from __future__ import absolute_import

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/sisgep1.db'

SECRET_KEY = 'seeeeeeeeeeeeeeeeeeeeeeeeeeeecret'

SECURITY_REGISTERABLE = True
SEND_REGISTER_EMAIL = False
SEND_PASSWORD_CHANGE_EMAIL = False
SEND_PASSWORD_RESET_NOTICE_EMAIL = False


SOCIAL_FACEBOOK = {
    'consumer_key': 'key',
    'consumer_secret': 'secret'
}
SOCIAL_TWITTER = {
    'consumer_key': 'key',
    'consumer_secret': 'secret'
}
