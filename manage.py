# coding: UTF-8
from __future__ import absolute_import

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand

import sisgep1
from sisgep1.manage import manager as sisge_manager

app = sisgep1.create_app()

manager = Manager(app)
manager.add_command('sisge', sisge_manager)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
