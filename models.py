# -*- coding: utf-8 -*-
from bd import db

class Homes_inf(db.Model):
    __tablesname__ = 'homes_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    info = db.Column(db.String(500))
    area = db.Column(db.String(500))
    price = db.Column(db.DECIMAL)
    place = db.Column(db.String(500))
    rent_type = db.Column(db.String(100))
    house_type = db.Column(db.String(100))
    house_acreage = db.Column(db.Integer)
    house_estate = db.Column(db.String(100))
    url = db.Column(db.String(500))
    publisher = db.Column(db.String(100))
    release_time = db.Column(db.DATETIME)
    mobile = db.Column(db.String(100))
    house_type1 = db.Column(db.String(100))
    house_type2 = db.Column(db.String(100))
