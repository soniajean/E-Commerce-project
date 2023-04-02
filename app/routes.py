
from . import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

from .api.services import get_products
from .models import User, Product

@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/sendit')
def sendIt():
    x = get_products(20)
    print("ADDED TO DB")
    p = Product(product_id=x['product_id'],title=x['product_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['product_image'])
    p.saveProduct()
    return render_template('index.html')