from .order_requests import 

USERS = [
    {
        "id": 1,
        "email": "jasonli99193@gmail.com",
        "password": "403234",
        "is_admin": True,
        "orderId": 0
    }
]

def get_all_users():
    return USERS

def get_single_user(id):

    requested_user = None

    for user in USERS:

        if user["id"] == id:
            requested_user = user
            break
