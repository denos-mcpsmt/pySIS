from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, CourseForm, CategoryForm
from flask_sqlalchemy import SQLAlchemy
from models.Student import Student
from models.User import User
from models.Course import Course
from models.Category import Category
from flask import Blueprint, request
from db import ScopedSession
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_bcrypt import Bcrypt
#from main import db, app
#app = Flask(__name__)
#app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
#db = SQLAlchemy(app)

bp = Blueprint('routes',__name__)
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'

@bp.route("/register", methods=['GET', 'POST'])
def register():
    session = ScopedSession()
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.password.data)
        hashed_password = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        session.add(user)
        session.commit()
        print("Registered!")
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    else:
        print("Not Registered!")
        print(form.errors)
    return render_template('register.html', title='Register', form=form)

@bp.route('/home')
def home():
    return render_template('home.html')




@bp.route('/login', methods=['GET', 'POST'])
def login():
    session = ScopedSession()
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = session.query(User).filter_by(email=email).first()

        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@bp.route('/catalog', methods=['GET'])
def catalog():
    catagories = Category.query.all()
    return render_template('interests.html',categories=catagories)

@bp.route('/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return render_template('courses.html',courses=courses)

@bp.route('/courses/new', methods=['GET', 'POST'])
def new_course():
    form = CourseForm()
    if request.method == 'POST':
        new_product = Course(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            image=request.form['image'],
            start_date=request.form['start_date'],
            end_date=request.form['end_date'],
            start_time=request.form['start_time'],
            end_time=request.form['end_time']
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('list_courses'))
    return render_template('new_course.html', title="New Course", form=form)

@bp.route('/catalog/new', methods=['GET', 'POST'])
def new_category():
    form = CategoryForm()
    if request.method == 'POST':
        new_category = Category(
            name=request.form['name'],
            description=request.form['description'],
            image=request.form['image']
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('catalog'))
    return render_template('new_category.html', title="New Category", form=form)