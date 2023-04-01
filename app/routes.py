
from . import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user


from .models import User

@app.route('/')
def homePage():
    return render_template('index.html')


