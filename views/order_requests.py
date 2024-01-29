import sqlite3
import json

ORDERS = [
    {
        "id": 1,
        "date": "01/20/2024",
        "productId": 1,
        "userId": 1
    }
]

def get_all_orders():
    return ORDERS

def get_single_order(id):

    requested_order = None

    for order in ORDERS:

        if order["id"] == id:
            requested_order = order
        
        return requested_order
    