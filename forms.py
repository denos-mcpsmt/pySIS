from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, SubmitField, PasswordField, FloatField ,TimeField, DateField, BooleanField, TextAreaField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from models.User import User
from models.Category import Category
from db import ScopedSession



class RegistrationForm(FlaskForm):
    session = ScopedSession()
    role = SelectField('Role', choices=[('student','Student'),('instructor','Instructor')])
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        session = ScopedSession()
        user = session.query(User).filter_by(username=str(username)).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
        else:
            print("Success - username")
    def validate_email(self, email):
        session = ScopedSession()
        user = session.query(User).filter_by(email=str(email)).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
        else:
            print("Success - email")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_email(self, email):
        session = ScopedSession()
        user = session.query(User).filter_by(email=email.data).first()
        if user is None:
            print('No user found with that email. Please register first.')


class UserUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

class CourseForm(FlaskForm):
    categories = SelectMultipleField('Categories', coerce=int)
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image')
    price = FloatField('Price')
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    min_students = IntegerField('Minimum Students')
    max_students = IntegerField('Maximum Students')
    submit = SubmitField('Create')

    def __init__(self,*args,**kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        session = ScopedSession()
        self.categories.choices = [(c.id, c.name) for c in session.query(Category).all()]

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image')
    submit = SubmitField('Create')