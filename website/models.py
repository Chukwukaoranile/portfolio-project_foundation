from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Volunteer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    address = db.Column(db.String(200))
    email = db.Column(db.String(150), unique=True)
    phone = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(200))
    profession = db.Column(db.String(50))


class Beneficiary(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    address = db.Column(db.String(200))
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(150), unique=True)
    diagnoses = db.Column(db.String(200))
    reason = db.Column(db.String(500))

'''

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

'''
