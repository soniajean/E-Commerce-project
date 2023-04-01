from flask import Blueprint
cart = Blueprint('cart', __name__, template_folder='cart_templates')
from flask_login import current_user, login_required


@cart.route('/add/<string:product>')
def addToCart(product):
    product = Product.query.filter_by(tile=title).first()
    if product:
        current_user.addToCart(product)
    return redirect(url_for('all_products.html'))

@cart.route('/remove/<string:product>')
def removeFromCart(product):
    product = Product.query.get(product)
    if product:
        current_user.removeFromCart(product)

    # return redirect(url_for('#'))