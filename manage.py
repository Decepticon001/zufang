# -*- coding: UTF-8 -*-

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from bd import db
from RentHouse import app

migrate = Migrate(app,db)
manage = Manager(app)
manage.add_command('db',MigrateCommand)

if __name__=='__main__':
    manage.run()