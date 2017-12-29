# -*- coding: UTF-8 -*-
import MySQLdb
import os

HOST = 'localhost'
DB_PORT = '3306'
DATABASE = 'homes'
USERNAME = 'root'
PASSWORD = '12341234'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOST,DB_PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
