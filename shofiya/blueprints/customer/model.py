from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref


class Customers(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    province = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    postal_code = db.Column(db.String(5), nullable=False)
    city_type = db.Column(db.String(10), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(15))
    bod = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    transactions = db.relationship(
        'Transactions', backref='customer', lazy=True)

    response_field = {
        'id': fields.Integer,
        'client_id': fields.Integer,
        'name': fields.String,
        'email': fields.String,
        'province': fields.String,
        'city': fields.String,
        'postal_code': fields.String,
        'city_type': fields.String,
        'street': fields.String,
        'phone': fields.String,
        'bod': fields.DateTime,
        'created_at': fields.DateTime,
        'updated_at': fields.DateTime,
    }

    def __init__(self, name, email, province, city, postal_code, city_type, street, phone, bod, client_id):
        self.name = name
        self.email = email
        self.province = province
        self.city = city
        self.postal_code = postal_code
        self.city_type = city_type
        self.street = street
        self.phone = phone
        self.bod = bod
        self.client_id = client_id

    def __repr__(self):
        return '<Customer %r>' % self.id
