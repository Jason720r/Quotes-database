from .category_requests import get_single_category


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
            break
    if requested_product is not None:
        matching_category = get_single_category(requested_product["typeId"])
        requested_product["type"] = matching_category
    
    return requested_product

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