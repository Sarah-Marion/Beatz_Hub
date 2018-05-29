from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()], render_kw={"placeholder": "Email"})
    username = StringField('Enter your username',validators = [Required()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators = [Required(),EqualTo('password_confirm',message = 'Passwords must match')], render_kw={"placeholder": "Password"})
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[Required()],render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ResetPassword(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()], render_kw={"placeholder": "Email"})
    submit = SubmitField('Reset Password')

class NewPassword(FlaskForm):
    password = PasswordField('Password',validators=[Required()], render_kw={"placeholder": "Password"})
    password_repeat = PasswordField('Repeat Password', validators=[Required(),EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Change Password')