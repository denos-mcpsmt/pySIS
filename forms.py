from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField ,TimeField, DateField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from models.User import User
from db import ScopedSession

class RegistrationForm(FlaskForm):
    session = ScopedSession()
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
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CourseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image')
    price = FloatField('Price')
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    submit = SubmitField('Create')

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image')
    submit = SubmitField('Create')