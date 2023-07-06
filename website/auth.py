from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Volunteer, Beneficiary

auth = Blueprint('auth', __name__)

@auth.route("/")
def home():
        return render_template("views.home")
'''
@auth.route('/beneficiary', methods=['GET', 'POST'])
def beneficiary():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        phone_number = request.form.get('phone_number')
        diagnoses = request.form.get('diagnoses')
        message = request.form.get('message')

        # To Check if any required field is missing
        if not email or not name or not phone_number or not diagnoses or not message:
            flash('Please fill in all the fields.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        else:
            # Rest of your code to create the Beneficiary instance
            # ...
            new_user = Volunteer(email=email, name=name, phone_number=phone_number, diagnoses=diagnoses)
            db.session.add(new_user)
            db.session.commit()
            flash('Successful! Thanks for joining us. We will reach out to you soon', category='success')
            return redirect(url_for('views.home'))

    return render_template("beneficiary.html")
'''
@auth.route('/beneficiary', methods=['GET', 'POST'])
def beneficiary():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('Name')
        phone_number = request.form.get('phone_number')
        diagnoses = request.form.get('diagnoses')
        message = request.form.get('message')

        # To Check if any required field is missing
        if not email or not name or not phone_number or not diagnoses or not message:
            flash('Please fill in all the fields.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        else:
            new_user = Volunteer(email=email, name=name, phone_number=phone_number, diagnoses=diagnoses)
            db.session.add(new_user)
            db.session.commit()
            flash('Successful! Thanks for joining us. We will reach out to you soon', category='success')
            return redirect(url_for('views.home'))

    return render_template("beneficiary.html")


@auth.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        profession = request.form.get('profession')
 
        user = Volunteer.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')

            new_user = Volunteer(email=email, name=name, phone_number=phone_number, address=address, profession=profession)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Successful! Thanks for joining us. We will reach out to you soon', category='success')
            return redirect(url_for('views.home'))

    return render_template("volunteer.html")


@auth.route("/about")
def about():
    return render_template("views.about")
