from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from ..models import Product


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.get('/product')
def getProduct():
    product = Product.query.all()
    productlist = [p.to_dict() for p in product]
    return {
        'status': 'ok',
        'data': productlist
    }

@auth.get('/product/<int:product_id>')
def getSingleproduct(product_id):
    p = Product.query.get(product_id)
    if p:
        product = p.to_dict()
        return {
            'status': 'ok',
            'data' : product
        }
    return {
        'status' : 'NOT ok',
        'message' : 'That product is not available!!'
    }

@auth.get('/product/item/<int:user_id>')
def getPostsByUser(user_id):
    product = Product.query.filter(Product.user_id == user_id).all()
    # Just so we can see the other example of the same query above:
    # posts = Post.query.filter_by(user_id == user_id).all()

    if product:
        return {
            'status' : 'ok',
            'product' : [p.to_dict() for p in product]
        }
    return {
        'status' : ' NOT ok',
        'message' : 'No product available to return from that ID'
    }
