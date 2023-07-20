from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from models.Student import Student
from flask import Blueprint, request
from db import ScopedSession
from datetime import datetime

#app = Flask(__name__)
#app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
#db = SQLAlchemy(app)

bp = Blueprint('routes',__name__)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    session = ScopedSession()
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        birthday = datetime.strptime(form.birthday.data,'%m-%d-%Y').date()
        student = Student(name=form.username.data, birthday=birthday, address=form.address.data)
        session.add(student)
        session.commit()
        return redirect(url_for('routes.home'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/home')
def home():
    return render_template('home.html')

def set_up_routes(app):
    app.register_blueprint(bp)

