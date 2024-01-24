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
    return CATEGORIES

def get_single_category():

    requested_category = None

    for category in CATEGORIES:

        if category["id"] == id:
            requested_category = category
    return requested_category