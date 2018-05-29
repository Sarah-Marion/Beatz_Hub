from ..models import User
from flask_wtf import FlaskForm
<<<<<<< HEAD
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

    
=======
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
>>>>>>> b3a4641111124f9321b173e15e0cbef1545eba88
