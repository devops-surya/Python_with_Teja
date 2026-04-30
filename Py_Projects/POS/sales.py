"""Sales and billing helper functions for the POS application."""
from inventory import get_item

CART: dict = {}

def add_item_to_cart(item_id:int, quantity:int) -> None:
    """Add an item to the cart.

    Args:
        item_id (int): Item id.
        quantity (int): Selected quantity.
    """
    # todo: Add items to the cart only if quantity is less than or equal to 
    # what is available in inventory
    CART[item_id] = quantity

def remove_item_from_cart(item_id:int) -> None:
    """Remove an item from the cart.

    Args:
        item_id (int): Item id.
    """
    del CART[item_id]

def generate_bill() -> int|float:
    """Calculate the total bill amount."""
    bill_amount = 0
    for item_id, quantity in CART.items():
        item = get_item(item_id)
        bill_amount += item['price'] * quantity
    return bill_amount

def finish_transaction():
    """Clear the cart after payment."""
    CART.clear()
    print("Payment received. Thanks for shopping")
