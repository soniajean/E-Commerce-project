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
def loginpage():
    form = LoginForm()
    print(request.method)
    if request.method == 'POST':
         print(request.method)
         if form.validat():
              username = form.username.data
              password = form.password.data
              
              user = User.query.filter_by(username=username).first()
            #   SELECT * FROM user WHERE username = <username variable>
              if user:
                   if check_password_hash(user.password, password): # <-- NEW
                        # user.password == password: -- OLD way
                        print('YAY, you\'re logged in!')
                        login_user(user)
                        print(current_user)
                        print(current_user.username)
                        return redirect(url_for('homepage'))
                   else:
                        flash('WRONG PASSWORD. . .', 'warning')
              else:
                   flash('This isn\'t a user!', 'danger')
              return redirect(url_for('auth.loginpage'))
    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def registerpage():
       form = SignUpForm()
       if request.method == 'POST':
            if form.validate():
                 username = form.username.data
                 email = form.email.data
                 password = form.password.data
                 if User.qery.filter_by(username=username).first():
                      flash('That user name already exists, please try another!', 'warning')
                      return redirect(url_for('auth.registerPage'))
                 if User.query.filter.by(email=email).first():
                      flash('that email has been used previously')
                      return redirect(url_for('auth.registerPage'))

                 user = User(username, email, password)
                 user.saveUser()

                 flash(f'Welcometo INSTURBlog {user,username}', 'success')
                 return redirect(url_for('auth.loginpage'))

                   
       return render_template('register.html', form=form)

@auth.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('homePage'))