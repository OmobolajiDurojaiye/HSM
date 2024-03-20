from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_service_provider = db.Column(db.Boolean, nullable=False)

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)




























class CustomerContactMessage(db.Model):
    __tablename__ = 'customercontactmessage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    messagebody = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<CustomerContactMessage(name='{self.name}', email='{self.email}', messagebody='{self.messagebody}')>"