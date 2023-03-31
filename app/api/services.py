import requests
import time

def get_products(products):
    url= f'https://fakestoreapi.com/products/{products}'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        product = {
        'product_id' : data["id"],
        'product_name' : data["title"],
        'price' : data["price"],
        'product_description' : data["description"],
        'category': data["category"],
        'product_image' : data["image"],
        'product_inventory' : data['rating'][1]["count"],
        }
        return product
    else:
        return None
