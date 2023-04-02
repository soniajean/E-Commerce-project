from models import Product
from api.services import get_products
from flask_login import current_user

x = get_products(12)
print(f"~~~~{x}")

p = Product(title=x['product_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['product_image'])

p.saveProduct()


