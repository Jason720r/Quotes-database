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
            p.image,
            p.price,
            p.deliveryTime,
            p.inStock,
            p.stockQuantity,
            p.typeId
        FROM product p
        """)
        # empty list
        products = []

        # convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        for row in dataset:
            # Create an product instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Product class above.
            product = Product(row['id'], row['title'], row['image'],
                              row['price'], row['deliveryTime'],
                              row['inStock'], row['stockQuantity'], row['typeId'])
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
            p.image,
            p.price,
            p.deliveryTime,
            p.inStock,
            p.stockQuantity,
            p.typeId
        FROM product p
        WHERE p.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        product = Product(data['id'], data['title'], data['image'],
                          data['price'], data['deliveryTime'], data['inStock'],
                          data['stockQuantity'], data['typeId'])
        return product.__dict__


def create_product(product):
    with sqlite3.connect("./commerce.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO product (title, image, price, deliveryTime, inStock, stockQuantity, typeId)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product['title'], product.get('image', ''), product['price'],
              product['deliveryTime'], product['inStock'], 
              product.get('stockQuantity', 0), product['typeId']))

        # This line is important to make sure changes are saved to the database
        conn.commit()

    # After inserting, fetch the last inserted ID to set it to the product
    product["id"] = db_cursor.lastrowid

    return product


def delete_product(id):
    with sqlite3.connect("./commerce.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM product
        WHERE id = ?
         """, (id, ))


def update_product(id, new_product):
    with sqlite3.connect("./commerce.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE product
            SET
                title = ?,
                image = ?,
                price = ?,
                deliveryTime = ?,
                inStock = ?,
                stockQuantity = ?
                typeId = ?
        WHERE id = ?      
        """, (new_product['title'], new_product['image'],
              new_product['price'], new_product['deliveryTime'],
              new_product['inStock'], new_product['stockQuantity'],
              new_product['typeId'], id,))
        
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        #404 response by main module
        return False
    else:
        #204 response by main module
        return True
def get_products_by_name(name):
     
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
        p.id,
        p.title,
        p.image,
        p.price,
        p.deliveryTime,
        p.inStock,
        p.stockQuantity,
        p.typeId
    FROM product p
    WHERE p.name = ?
    """, ( name, ))
    
    products = []
    dataset = db_cursor.fetchall()

    for row in dataset:
        product = Product(row['id'], row['title'], row['image'],
                              row['price'], row['deliveryTime'],
                              row['inStock'], row['stockQuantity'], row['typeId'])
        products.append(product.__dict__)
    
    return products