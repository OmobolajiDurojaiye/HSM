from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(120), nullable=False, default='customer')

class Service(db.Model):
    __tablename__ = 'services'
    service_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.String(50), nullable=False)
    # Define relationship with User model
    provider = db.relationship('User', backref=db.backref('services', lazy=True))

class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    booking_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    # Define relationships with User and Service models
    customer = db.relationship('User', foreign_keys=[customer_id], backref=db.backref('bookings_as_customer', lazy=True))
    provider = db.relationship('User', foreign_keys=[provider_id], backref=db.backref('bookings_as_provider', lazy=True))
    service = db.relationship('Service', backref=db.backref('bookings', lazy=True))


class Review(db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    # Define relationships with User and Service models
    reviewer = db.relationship('User', foreign_keys=[reviewer_id], backref=db.backref('reviews_given', lazy=True))
    provider = db.relationship('User', foreign_keys=[provider_id], backref=db.backref('reviews_received', lazy=True))
    service = db.relationship('Service', backref=db.backref('reviews', lazy=True))

class CustomerContactMessage(db.Model):
    __tablename__ = 'customercontactmessage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    messagebody = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<CustomerContactMessage(name='{self.name}', email='{self.email}', messagebody='{self.messagebody}')>"