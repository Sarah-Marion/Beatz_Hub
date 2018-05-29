from flask import render_template, redirect, request, url_for, flash
from flask_login import UserMixin, current_user, login_user, logout_user
from .import auth
from ..import db
from ..models import User
from .forms import LoginForm, RegisterForm


@auth.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    title = "Login"
    Login = LoginForm()

    if Login.validate_on_submit:
        user = User.query.filter_by(email = Login.email.data).first()
        if user is not None and user.verify_password(Login.password.data):
            login_user(user, Login.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid, Try again')

    return render_template('auth/login.html', Login = Login, title=title)



@auth.route('/register', methods=['GET', 'POST'])
def register():
    title= "Register Account"
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password = form.password.data, is_admin=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title=title, form= form)


 
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))