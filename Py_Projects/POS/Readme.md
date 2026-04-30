# Store POS - Python Terminal Billing Project

A beginner-friendly **Point of Sale** project made with simple Python. This guide explains the project first, then gives a clear order for writing the code.

The project runs in the terminal. It lets the user add inventory items, select items for sale, calculate the bill, confirm payment, and clear the cart.

---

## Project Idea

Imagine a small shop counter. Before billing a customer, the shop needs a list of items. After items are added to inventory, the cashier can select item ids, enter quantities, and generate the final bill.

This project teaches that real-world process using only Python basics.

---

## What This Project Can Do

- Add items to inventory
- Display all inventory items
- Display items available for sale
- Add selected items to a cart
- Generate a bill from item price and quantity
- Confirm payment
- Clear the cart after transaction
- Exit the program

---

## Important Note

The current version stores data only in memory.

That means:

- No database is used
- No file saving is used
- Inventory starts empty when the program starts
- Added items disappear when the program closes

This is intentional because the project is made for learning Python fundamentals first.

---

## Python Concepts Used

| Concept | Used In Project |
|---|---|
| Variables | store names, prices, quantities, menu choices |
| Lists | `ITEMS` stores all inventory products |
| Dictionaries | each product is stored as a dictionary |
| Functions | each task is separated into a function |
| Loops | menus repeat with `while True` |
| Conditional statements | menu routing uses `if`, `elif`, `else` |
| Type casting | `int()` and `float()` convert user input |
| Imports | `pos.py` imports functions from other files |
| String formatting | bill and item details are printed in terminal |

---

## Folder Structure

```text
POS/
|
|-- pos.py          # Main file: menus and user flow
|-- inventory.py    # Inventory list and item functions
|-- sales.py        # Cart and billing functions
|-- Readme.md       # Markdown explanation
|-- README.html     # Visual HTML explanation
```

---

## File Explanation

### `pos.py`

This is the entry point of the app.

It contains:

- `main_menu()`
- `inventory_menu()`
- `sale_menu()`

This file controls what the user sees in the terminal.

### `inventory.py`

This file manages product data.

It contains:

- `ITEMS`
- `add_item()`
- `get_item()`
- `find_item()`
- `delete_item()`
- `update_item()`
- `search_item_by_name()`
- `print_inventory_menu()`
- `print_sales_menu()`

### `sales.py`

This file manages cart and billing.

It contains:

- `CART`
- `add_item_to_cart()`
- `remove_item_from_cart()`
- `generate_bill()`
- `finish_transaction()`

---

## Data Structure

### Inventory

Inventory is stored in a list called `ITEMS`.

At program start, it is empty:

```python
ITEMS = []
```

When a product is added, the program stores it like this:

```python
{
    "id": 1,
    "name": "Pendrive",
    "description": "64GB USB storage device",
    "price": 599.0,
    "quantity": 30
}
```

### Cart

Cart is stored as a dictionary called `CART`.

```python
CART = {}
```

Example:

```python
CART = {
    1: 2,
    2: 1
}
```

This means:

- Item id `1` has quantity `2`
- Item id `2` has quantity `1`

---

## Full Process Flow

```text
Start program
|
|-- Main Menu
|   |
|   |-- 1. Sale
|   |   |
|   |   |-- Show items available for sale
|   |   |-- Ask item id
|   |   |-- Ask item quantity
|   |   |-- Add item to cart
|   |   |-- Ask if more sale items are needed
|   |   |-- Generate bill
|   |   |-- Confirm payment
|   |   |-- Clear cart
|   |
|   |-- 2. Inventory
|   |   |
|   |   |-- Show current inventory
|   |   |-- Ask item name
|   |   |-- Ask item description
|   |   |-- Ask price
|   |   |-- Ask stock quantity
|   |   |-- Add item to inventory
|   |   |-- Ask if more items are needed
|   |
|   |-- 3. Exit
|       |
|       |-- Close application
```

---

## Screenshots / Terminal Images

These are terminal-style screenshots showing the full project flow.

---

## Quick Examples

Use these examples while explaining the project in class. Every action starts from the main menu so students understand where the feature begins.

### Example 1 - Add a Product

This example adds a pendrive to inventory.

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 2
Opening Inventory

id      item name       price   stock

Enter item name: Pendrive
Enter item description: 64GB USB storage device
Enter item price: 599
Enter stock quantity: 30
Add another item? Enter Y for yes and N for no: n
```

After this input, the item stored in `ITEMS` looks like this:

```python
{
    "id": 1,
    "name": "Pendrive",
    "description": "64GB USB storage device",
    "price": 599.0,
    "quantity": 30
}
```

### Example 2 - Add One More Product

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 2
Opening Inventory

id      item name       price   stock
1       Pendrive        599.0   30

Enter item name: Hard Disk
Enter item description: 1TB external hard disk
Enter item price: 3499
Enter stock quantity: 10
Add another item? Enter Y for yes and N for no: n
```

Now inventory has two products:

```text
id      item name               price   stock
1       Pendrive                599.0   30
2       Hard Disk               3499.0  10
```

### Example 3 - Add Product to Cart

If the customer buys two pendrives:

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 1
Opening Sale

id      item name       price
1       Pendrive        599.0
2       Hard Disk       3499.0

Enter item id: 1
Enter item quantity: 2
Add another sale item? Enter Y for yes and N for no: n
```

The cart becomes:

```python
CART = {
    1: 2
}
```

### Example 4 - Bill Calculation

```text
Pendrive   = 599.0 x 2
Total bill = 1198.0
```

Terminal output:

```text
Total bill amount is 1198.0
Press Enter to confirm payment.
Payment received. Thanks for shopping
```

---

## Step-by-Step Screenshots

Follow these screens in order while presenting the project.

---

## Screen 1 - Program Start / Main Menu

Run the project from the POS folder:

```text
PS D:\Devops\Python\Py_Projects\POS> python pos.py

===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: _
```

---

## Screen 2 - Select Inventory from Main Menu

Because inventory starts empty, first go to the main menu and select option `2`.

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 2
Opening Inventory

id      item name       price   stock

Enter item name: _
```

---

## Screen 3 - Add First Product: Pendrive

The user enters item name, description, price, and stock quantity.

```text
Enter item name: Pendrive
Enter item description: 64GB USB storage device
Enter item price: 599
Enter stock quantity: 30
Add another item? Enter Y for yes and N for no: y
```

What happens:

- The user selected `2` from the main menu
- `add_item()` receives the item details
- `next_item_id` becomes `1`
- a product dictionary is created
- the dictionary is appended to `ITEMS`

---

## Screen 4 - Return to Main Menu and Select Inventory Again

To add another product separately, go back to the main menu and select `2` again.

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 2
Opening Inventory

id      item name       price   stock
1       Pendrive        599.0   30

Enter item name: _
```

---

## Screen 5 - Add Second Product: Hard Disk

```text
id      item name       price   stock
1       Pendrive        599.0   30

Enter item name: Hard Disk
Enter item description: 1TB external hard disk
Enter item price: 3499
Enter stock quantity: 10
Add another item? Enter Y for yes and N for no: n
```

---

## Screen 6 - Inventory After Adding Products

When the user enters `n`, the inventory list is shown again.

```text
id      item name               price   stock
1       Pendrive                599.0   30
2       Hard Disk               3499.0  10
```

---

## Screen 7 - Return to Main Menu and Select Sale

After adding products, return to the main menu and select option `1` for sale.

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 1
Opening Sale

id      item name               price
1       Pendrive                599.0
2       Hard Disk               3499.0

Enter item id: _
```

---

## Screen 8 - Add First Item to Cart

```text
Enter item id: 1
Enter item quantity: 2
Add another sale item? Enter Y for yes and N for no: y
```

At this point, the cart becomes:

```python
CART = {
    1: 2
}
```

---

## Screen 9 - Add Second Item to Cart

```text
id      item name               price
1       Pendrive                599.0
2       Hard Disk               3499.0

Enter item id: 2
Enter item quantity: 1
Add another sale item? Enter Y for yes and N for no: n
```

Now the cart becomes:

```python
CART = {
    1: 2,
    2: 1
}
```

---

## Screen 10 - Bill Output

When the user enters `n`, the program generates the bill.

```text
Total bill amount is 4697.0
Press Enter to confirm payment.
Payment received. Thanks for shopping
```

Bill calculation:

```text
Pendrive                599.0 x 2 = 1198.0
Hard Disk              3499.0 x 1 = 3499.0
--------------------------------------------
Total bill                         4697.0
```

---

## Screen 11 - Return to Main Menu and Exit

After payment, the program returns to the main menu. Select option `3` to exit.

```text
===== STORE POS =====

1. Sale
2. Inventory
3. Exit

Choose an option: 3
Thank you. Goodbye
```

---

## Function Reference

| File | Function | What It Does |
|---|---|---|
| `pos.py` | `main_menu()` | Shows the main menu |
| `pos.py` | `inventory_menu()` | Takes item details and adds inventory |
| `pos.py` | `sale_menu()` | Takes sale item id and quantity |
| `inventory.py` | `add_item()` | Adds a new item dictionary to `ITEMS` |
| `inventory.py` | `get_item()` | Returns an item by id |
| `inventory.py` | `find_item()` | Finds the item index by id |
| `inventory.py` | `delete_item()` | Deletes an item from inventory |
| `inventory.py` | `update_item()` | Updates item details |
| `inventory.py` | `search_item_by_name()` | Searches item by name |
| `inventory.py` | `print_inventory_menu()` | Prints id, name, price, and stock |
| `inventory.py` | `print_sales_menu()` | Prints id, name, and price |
| `sales.py` | `add_item_to_cart()` | Adds item id and quantity to cart |
| `sales.py` | `remove_item_from_cart()` | Removes item from cart |
| `sales.py` | `generate_bill()` | Calculates total bill amount |
| `sales.py` | `finish_transaction()` | Clears cart after payment |

---

## How to Explain Before Writing Code

### Step 1 - Explain the Shop Problem

A shop needs a simple billing system. The system must know what items are available and how much each item costs.

### Step 2 - Explain Inventory

Inventory is a list. Each item in the list is a dictionary.

```python
ITEMS = []
```

Each dictionary stores:

- id
- name
- description
- price
- quantity

### Step 3 - Explain Cart

The cart stores what the customer wants to buy.

```python
CART = {}
```

The item id is the key. The selected quantity is the value.

### Step 4 - Explain Billing

For each item in the cart:

```text
item total = item price x selected quantity
```

Then all item totals are added together.

### Step 5 - Explain Menus

The project has one main menu:

```text
1. Sale
2. Inventory
3. Exit
```

The main menu decides which function should run.

---

## Best Code Writing Order

Write the project in this order:

```text
1. Create inventory.py
2. Create ITEMS list
3. Write add_item()
4. Write find_item()
5. Write get_item()
6. Write print_inventory_menu()
7. Write print_sales_menu()
8. Create sales.py
9. Create CART dictionary
10. Write add_item_to_cart()
11. Write generate_bill()
12. Write finish_transaction()
13. Create pos.py
14. Import inventory and sales functions
15. Write inventory_menu()
16. Write sale_menu()
17. Write main_menu()
18. Run and test the complete project
```

---

## Current Limitations

This version is good for learning, but it is still basic.

Current limitations:

- Inventory starts empty every time
- Data is not stored in a file or database
- Stock quantity is not reduced after sale
- Cart does not check if enough stock is available
- Wrong item id can cause an error during bill generation
- `delete_item()`, `update_item()`, and `search_item_by_name()` exist but are not connected to menu options

---

## Future Improvements

Good next upgrades:

- Add default products
- Save inventory to a file
- Reduce stock after sale
- Check stock before adding to cart
- Print a detailed receipt
- Add discount support
- Add GST/tax calculation
- Connect delete, update, and search to the menu
- Store sales history
- Create a GUI or web version

---

## How to Run

Open terminal in the POS folder:

```powershell
cd D:\Devops\Python\Py_Projects\POS
python pos.py
```

Then use:

```text
1. Sale
2. Inventory
3. Exit
```

---

## Summary

This POS project is a simple but useful Python practice project.

Students first understand the real billing process, then convert each step into code:

- inventory becomes a list
- item details become dictionaries
- cart becomes a dictionary
- billing becomes a loop
- user choices become menu conditions

That makes the project easy to explain, easy to code, and easy to improve later.
