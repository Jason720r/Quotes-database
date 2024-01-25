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

def get_single_category(id):

    requested_category = None

    for category in CATEGORIES:

        if category["id"] == id:
            requested_category = category

    return requested_category

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