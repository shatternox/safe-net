from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_pass', message="Password must be the same")])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
	    if User.query.filter_by(email=self.email.data).first():
                raise ValidationError('Email already registered!')

    def validate_username(self, username):
	    if User.query.filter_by(username=self.username.data).first():
                raise ValidationError('Username taken!')
