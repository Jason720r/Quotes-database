import sqlite3
import json
from models import Category

CATEGORIES = [
    {
        "id": 1,
        "type": "Furniture"
    },
    {
        "id": 2,
        "type": "Kitchen"
    }
]

def get_all_categories():
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.type
        FROM category c
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Category(row['id'], row['type'])

            categories.append(category.__dict__)
        return categories

def get_single_category(id):
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
            c.id,
            c.type
        FROM category c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        category = Category(data['id'], data['type'])

        return category.__dict__


def create_category(category):

    max_id = CATEGORIES[-1]["id"]

    new_id = max_id + 1

    category["id"] = new_id

    CATEGORIES.append(category)

    return category

def delete_category(id):

    category_index = -1

    for index, category in enumerate(CATEGORIES):
        if category["id"] == id:

            category_index = index
        
    if category_index >= 0:
        CATEGORIES.pop(category_index)

def update_category(id, new_category):

    for index, category in enumerate(CATEGORIES):
        if category["id"] == id:

            CATEGORIES[index] = new_category
            break