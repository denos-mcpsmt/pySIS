from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, CourseForm, CategoryForm, UserUpdateForm
from flask_sqlalchemy import SQLAlchemy
from models.User import User, Student, Instructor
from models.Course import Course
from models.Category import Category
from flask import Blueprint, request
from db import ScopedSession
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from flask_bcrypt import Bcrypt
from utils.db_utils import get_courses_by_category

#from main import db, app
#app = Flask(__name__)
#app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
#db = SQLAlchemy(app)

bp = Blueprint('routes',__name__)
bcrypt = Bcrypt()
#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'

@bp.route("/register", methods=['GET', 'POST'])
def register():
    session = ScopedSession()
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.password.data)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        if form.role.data == 'student':
            user = Student(username=form.username.data, email=form.email.data, password=hashed_password)
        elif form.role.data == 'instructor':
            user = Instructor(username=form.username.data, email=form.email.data, password=hashed_password)

        session.add(user)
        session.commit()
        print("Registered!")
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('routes.login'))
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
    print("val: "+str(form.validate_on_submit()))
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    if form.validate_on_submit():
        email = form.email.data
        user = session.query(User).filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            print("User Authenticated")
            return redirect(next_page) if next_page else redirect(url_for('routes.home'))

    else:
        print('Login Unsuccessful. Please check username and password')
        print(form.errors)
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@bp.route('/account')
@login_required
def account():
    return render_template('account.html')

@bp.route('/account/edit', methods=['GET', 'POST'])
@login_required
def edit_account():
    form = UserUpdateForm()
    session = ScopedSession()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        session.commit()
        print('Your account has been updated!')
        return redirect(url_for('routes.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('edit_account.html', form=form)

@bp.route('/account/courses')
@login_required
def user_courses():
    # Assuming that the User model has a relationship to the Course model
    courses = current_user.courses
    return render_template('user_courses.html', courses=courses)

@bp.route('/catalog', methods=['GET'])
def catalog():
    session = ScopedSession()
    categories = session.query(Category).all()
    return render_template('interests.html',categories=categories)

@bp.route('/course/<int:course_id>')
def course_detail(course_id):
    session = ScopedSession()
    course = session.query(Course).filter_by(id=course_id).first()
    return render_template('course_detail.html', title=course.name, course=course)

@bp.route('/courses/<int:category_id>', methods=['GET'])
def list_courses(category_id):
    session = ScopedSession()
    category = session.query(Category).filter_by(id=category_id).first()
    courses = get_courses_by_category(category_id)
    return render_template('courses.html',courses=courses,category=category)

@bp.route('/courses/new', methods=['GET', 'POST'])
def new_course():
    session = ScopedSession()
    form = CourseForm()
    if request.method == 'POST':
        new_course = Course(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            image=request.form['image'],
            start_date=datetime.strptime(request.form['start_date'], '%Y-%M-%d').date(),
            end_date=datetime.strptime(request.form['end_date'], '%Y-%M-%d').date(),
            start_time=datetime.strptime(request.form['start_time'], '%H:%M').time(),
            end_time=datetime.strptime(request.form['end_time'], '%H:%M').time()
        )
        for category_id in form.categories.data:
            category = session.query(Category).filter_by(id=category_id).first()
            new_course.categories.append(category)
        cat_id = form.categories.data[0]
        session.add(new_course)
        session.commit()
        return redirect(url_for('routes.list_courses', category_id=cat_id))
    return render_template('new_course.html', title="New Course", form=form)

@bp.route('/course/enroll/<int:course_id>')
def enroll(course_id):
    return render_template('temp.html', title="Under Construction")

@bp.route('/catalog/new', methods=['GET', 'POST'])
def new_category():
    session = ScopedSession()
    form = CategoryForm()
    if request.method == 'POST':
        new_category = Category(
            name=request.form['name'],
            description=request.form['description'],
            image=request.form['image']
        )
        session.add(new_category)
        session.commit()
        return redirect(url_for('routes.catalog'))
    return render_template('new_category.html', title="New Category", form=form)