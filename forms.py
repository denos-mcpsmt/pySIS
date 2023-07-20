from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    birthday = StringField('Birthday', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Sign Up')