from .order_requests import get_single_order
import sqlite3
import json
from models import User
USERS = [
    {
        "id": 1,
        "email": "jasonli99193@gmail.com",
        "password": "403234",
        "first_name": "Jason",
        "last_name": "Li",
        "is_admin": True,
        "orderId": 0
    }
]

def get_all_users():
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.email,
            u.password,
            u.firstName,
            u.lastName,
            u.isAdmin,
            u.orderId
        FROM U u  
        """)

        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            user = User(row['id'], row['email'], row['password'],
                        row['firstName'], row['lastName'], row['isAdmin'],
                        row['orderId'])
            users.append(user.__dict__)
        return users

def get_single_user(id):

    requested_user = None

    for user in USERS:

        if user["id"] == id:
            requested_user = user
            break
