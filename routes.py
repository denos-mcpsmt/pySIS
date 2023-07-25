from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models.Student import Student
from models.User import User
from flask import Blueprint, request
from db import ScopedSession
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_bcrypt import Bcrypt

#app = Flask(__name__)
#app.config['SECRET_KEY'] = b'\xd4\xc5\xf2\xae\xaa\xb7\xc7\xd9}\xf3}\xebHG\xa4\x96'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
#db = SQLAlchemy(app)

bp = Blueprint('routes',__name__)
login_manager = LoginManager()
login_manager.init_app(bp)
login_manager.login_view = 'login'

@bp.route("/register", methods=['GET', 'POST'])
def register():
    session = ScopedSession()
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        session.add(user)
        session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/home')
def home():
    return render_template('home.html')

def set_up_routes(app):
    app.register_blueprint(bp)

@login_manager.user_loader
def load_user(user_id):
    session = ScopedSession()
    return session.query(User).get(int(user_id))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        session = ScopedSession()
        user = session.query(User).filter_by(username=username).first()

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