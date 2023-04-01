from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import logout_user, login_user, current_user
from werkzeug.security import check_password_hash

from .forms import SignUpForm, LoginForm
from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/test')
def login():
    return render_template('test.html')


@auth.route('/login', methods=['GET', 'POST'])    
def loginPage():
    form = LoginForm()
    if request.method == 'POST':
        print()
        if form.validate():
            username = form.username.data
            password = form.username.data
            print(username, password)


@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)
            user = User(username, email, password)
            user.saveUser()
            return redirect(url_for('loginPage'))
    return render_template('register.html', form=form)

@auth.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('homePage'))