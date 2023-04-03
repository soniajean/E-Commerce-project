from flask import Blueprint, render_template, request, url_for, redirect, flash
cart = Blueprint('cart', __name__, template_folder='cart_templates')
from flask_login import current_user, login_required
from app.models import User, Product


@cart.route('/my-cart')
def viewMyCart():
    products = current_user.carted
    cart_total = 0
    for p in products:
        cart_total += (p.price)
    print(products)
    return render_template('my_cart.html', products=products, total=cart_total)

@cart.route('/add/<int:product_id>')
def addToCart(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    product.saveToCart(current_user)
    product_name=product.title
    flash(f"{product_name} has been added!")
    return redirect(url_for('homePage'))

@cart.route('/view-singe-item/<int:product_id>')
def viewSingleProduct(product_id):
    product = Product.query.get(product_id)
    return render_template('single_product.html',product=product)

@cart.route('/view-all-products')
def viewAllProducts():
    products = Product.query.order_by(Product.product_id).all()
    return render_template('all_products.html', products=products)