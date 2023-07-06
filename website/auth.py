from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Volunteer, Beneficiary
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, mail   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/beneficiary', methods=['GET', 'POST'])
def beneficiary():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        phone_number = request.form.get('phone_number')
        diagnoses = request.form.get('diagnoses')
        message = request.form.get('message')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Beneficiary.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_beneficiary = Beneficiary(email=email, name=name, phone_number=phonenumber, diagnoses=diagnoses, message=message, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_beneficiary)
            db.session.commit()
            login_user(new_beneficiary, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("beneficiary.html", user=current_user)

@auth.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        profession = request.form.get('profession')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Volunteer.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = Volunteer(email=email, name=name, phone_number=phone_number, profession=profession, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("volunteer.html", user=current_user)


'''
@auth.route('/volunteer', methods=['GET', 'POST'])                      def volunteer():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        profession = request.form.get('profession')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
            if user:                                                                  flash('Email already exists.', category='error')                  elif len(email) < 4:                                                      flash('Email must be greater than 3 characters.', category='error')                                                                     elif len(first_name) < 2:                                                 flash('First name must be greater than 1 character.', category='error')                                                                 elif password1 != password2:                                              flash('Passwords don\'t match.', category='error')                elif len(password1) < 7:                                                  flash('Password must be at least 7 characters.', category=
'error')
        else:                                                                     new_volunteer = Volunteer(email=email, name=name, phone_number=phone_number, profession=profession, password=generate_password_hash(password1, method='sha256'))
        db.session.add(new_volunteer)
        db.session.commit()
        login_volunteer(new_volunteer, remember=True)
        flash('Account created!', category='success')                         return redirect(url_for('views.home'))                                                                                              return render_template("volunteer.html", user=current_user)

'''

'''        
@auth.route("/volunteer", methods=["GET", "POST"])
def volunteer():
    return render_template("views.volunteer", user=current_volunteer)
''' 

'''
@auth.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Send email
        send_email(mail, name, email, message)

        # Store in database
        save_contact(name, email, message)

        return "Thank you for contacting us! We will get back to you soon."

    return render_template('views.contact')
def send_email(mail, name, email, message):
    msg = Message("Contact Form Submission", sender=email, recipients=["chika@chukwukaoranile.tech"])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

def save_contact(name, email, message):
    # Save the contact form data in the database
    # You can use the Note model or create a separate Contact model for this purpose
    contact = Contact(name=name, email=email, message=message)
    db.session.add(contact)
    db.session.commit()
'''

@auth.route("/about")
def about():
    return render_template("views.about")
