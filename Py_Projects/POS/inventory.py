"""Inventory helper functions for the POS application."""

# ITEMS: list[dict[str, object]] = []
ITEMS: list[dict] = []


def add_item(
        name: str,
        description: str,
        price: int | float,
        quantity: int) -> bool:
    """Add a new item to inventory.

    Args:
        name (str): Item name.
        description (str): Item description.
        price (int | float): Item price.
        quantity (int): Available quantity.

    Returns:
        bool: True when values are valid, False otherwise.
    """
    # validate
    # Todo: As of now we are sending only True or False but not the reason
    #       when values are invalid. This needs to be fixed
    if price < 1 and quantity < 1:
        return False

    next_item_id = len(ITEMS) + 1
    ITEMS.append({
        "id": next_item_id,
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity
    })
    return True

def get_item(item_id:int) -> dict|None:
    """Get one item from inventory.

    Args:
        item_id (int): Item id.

    Returns:
        dict | None: Item details when found, otherwise None.
    """
    item_index = find_item(item_id)
    if item_index is None:
        return None
    return ITEMS[item_index]


def find_item(item_id:int) -> int|None:
    """Find an item index using item id.

    Args:
        item_id (int): Item id to search.

    Returns:
        int | None: Item index if found, otherwise None.
    """
    item_index = None
    for row_number, item in enumerate(ITEMS):
        if item['id'] == item_id:
            item_index = row_number
            break
    return item_index

def delete_item(item_id:int) -> bool:
    """Delete an item from inventory.

    Args:
        item_id (int): Item id.

    Returns:
        bool: True if deleted, False otherwise.
    """
    item_index = find_item(item_id)
    if item_index == None:
        return False
    del ITEMS[item_index]
    return True

def update_item(
        item_id:int,
        name: str,
        description: str,
        price: int | float,
        quantity: int) -> bool:
    """Update an existing inventory item.

    Args:
        item_id(int): Item id.
        name (str): Item name.
        description (str): Item description.
        price (int | float): Item price.
        quantity (int): Available quantity.

    Returns:
        bool: True when values are valid, False otherwise.
    """
    if price < 1 and quantity < 1:
        return False
    item_index = find_item(item_id)
    if item_index == None:
        return False
        
    ITEMS[item_index] = {
        "id": item_id,
        "name": name,
        "description": description,
        "price": price,
        "quantity": quantity
    }

def search_item_by_name(name: str) -> list[dict]:
    """Search inventory items by name.

    Args:
        name (str): Item name or partial name.

    Returns:
        list[dict]: Matching items.
    """
    matched_items = []
    for item in ITEMS:
        if name.lower() in item['name'].lower():
            matched_items.append(item)
    return matched_items

def print_inventory_menu():
    """Print all inventory items with quantity."""
    print("id\titem name\tprice\tstock")
    for item in ITEMS:
        print(f"{item['id']}\t{item['name']}\t{item['price']}\t{item['quantity']}")

def print_sales_menu():
    """Print all items available for sale."""
    print("id\titem name\tprice")
    for item in ITEMS:
        print(f"{item['id']}\t{item['name']}\t{item['price']}")
