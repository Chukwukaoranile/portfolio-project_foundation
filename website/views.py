from flask import Blueprint, render_template, request, flash
from .models import  Volunteer, Beneficiary


views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("home.html")

@views.route('/beneficiary', methods=['GET', 'POST'])
def beneficiary():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        diagnoses = request.form.get('diagnoses')
        message = request.form.get('message')
        
        new_beneficiary = Beneficiary.query.filter_by(email=email).first()
        if new_beneficiary:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        
            new_beneficiary = Beneficiary(email=email, name=name, phone_number=phone_number, diagnoses=diagnoses, message=message)
            db.session.add(new_beneficiary)
            db.session.commit()
            flash('Thanks for Joining us, we will reach out to you!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("beneficiary.html")

@views.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        phone_number = request.form.get('phone_number')
        address = request.form.get('address')
        profession = request.form.get('profession')
 
        new_volunteer = Volunteer.query.filter_by(email=email).first()
        if new_volunteer:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')

            new_volunteer = Volunteer(email=email, name=name, phone_number=phone_number, profession=profession)
            db.session.add(new_volunteer)
            db.session.commit()
            flash('Successful! Thanks for joining us. We will reach out to you soon', category='success')
            return redirect(url_for('views.home'))

    return render_template("volunteer.html")


@views.route("/about")
def about():
    return render_template("about.html")
