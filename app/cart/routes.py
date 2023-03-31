from flask import Blueprint
cart = Blueprint('cart', __name__, template_folder='cart_templates')
from flask_login import current_user, login_required
