from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Volunteer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(100))
    phone_number = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(200))
    profession = db.Column(db.String(50))
    password = db.Column(db.String(150))


class Beneficiary(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(100))
    phone_number = db.Column(db.Integer, unique=True)
    diagnoses = db.Column(db.String(200))
    message = db.Column(db.String(500))
    password = db.Column(db.String(150))

'''
class Note(db.Model):                                                     id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())      user_id = db.Column(db.Integer, db.ForeignKey('user.id'))                                                                               class User(db.Model, UserMixin):                                          id = db.Column(db.Integer, primary_key=True)                          email = db.Column(db.String(150), unique=True)                        password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(150))
    message = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())


    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message  '''
