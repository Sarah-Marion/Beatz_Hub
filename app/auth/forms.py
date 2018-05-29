from ..models import User
from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class LoginForm(FlaskForm):
    email= StringField('Email',validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField("Login")

def validate_email(form,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

def validate_username(form,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[Required(), validate_username])
    email = StringField("Email", validators=[Email(), Required(), validate_email])
    password = PasswordField('Password', validators =[Required(),
    EqualTo("password_confirm", message="Password must match")])
    password_confirm = PasswordField('Confirm Password', validators = [Required()])

    submit = SubmitField('Sign Up')

    