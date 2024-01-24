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
    return PRODUCTS

def get_single_product(id):

    requested_product = None

    for product in PRODUCTS:

        if product["id"] == id:
            requested_product = product
    
    return requested_product