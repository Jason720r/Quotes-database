from .order_requests import get_single_order
import sqlite3
import json
from models import User


def get_all_users():
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.firstName,
            u.lastName,
            u.isAdmin,
            u.orderId,
            u.email,
            u.password
        FROM U_new u  
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
    with sqlite3.connect("./commerce.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
        SELECT
        u.id,
        u.firstName,
        u.lastName,
        u.isAdmin,
        u.orderId,
        u.email,
        u.password
    FROM U_new u
    WHERE p.id = ?
    """, ( id, ))

    data = db_cursor.fetchone()

    user = User(data['id'], data['email'], data['password'],
                        data['firstName'], data['lastName'], data['isAdmin'],
                        data['orderId'])
    return user.__dict__
