
from app import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user


from .models import User

@app.route('/')
def homePage():
    users = User.query.all()
    # users = User.query.limit(20)
    follow_set = set()

    if current_user.is_authenticated:
        users_following = current_user.following.all()
        print(users_following)
        for u in users_following:
            follow_set.add(u.id)
        for u in users:
            if u.id in follow_set:
                u.flag = True

    

    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
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
11:53
@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()
    if request.method == 'POST':
        print()
        if form.validate():
            username = form.username.data
            password = form.username.data
            print(username, password)
