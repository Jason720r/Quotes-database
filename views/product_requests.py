from .category_requests import get_single_category
import sqlite3
import json
from models import Product


PRODUCTS = [
    {
        "id": 1,
        "typeId": 1,
        "title": "rug",
        "price": 25.99,
        "deliveryTime": "2 weeks",
        "inStock": 3

    },
    {
        "id": 2,
        "typeId": 1,
        "title": "couch",
        "price": 30.99,
        "deliveryTime": "2 weeks",
        "inStock": 2

    }
]

def get_all_products():
    
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.price,
            p.deliveryTime,
            p.inStock,
            p.typeId
        FROM product p
        """)
        #empty list
        products = []

        #convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:
            # Create an product instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Product class above.
            product = Product(row['id'], row['title'], row['price'],
                              row['deliveryTime'], row['inStock'],
                              row['typeId'])
            products.append(product.__dict__)
        return products

def get_single_product(id):
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
            p.id,
            p.title,
            p.price,
            p.deliveryTime,
            p.inStock,
            p.typeId
        FROM product p
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        product = Product(data['id'], data['title'], data['price'],
                              data['deliveryTime'], data['inStock'],
                              data['typeId'])
        return product.__dict__

def create_product(product):

    max_id = PRODUCTS[-1]["id"]

    new_id = max_id + 1

    product["id"] = new_id

    PRODUCTS.append(product)

    return product

def delete_product(id):

    product_index = -1

    for index, product in enumerate(PRODUCTS):
        if product["id"] == id:

            product_index = index
    
    if product_index >= 0:
        PRODUCTS.pop(product_index)

def update_product(id, new_product):

    for index, product in enumerate(PRODUCTS):
        if product["id"] == id:

            PRODUCTS[index] = new_product
            break