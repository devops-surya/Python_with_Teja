"""Main entry point for the POS terminal application."""
from inventory import (
    print_sales_menu, 
    print_inventory_menu,
    add_item,
    delete_item,
    update_item,
    search_item_by_name
)

from sales import (
    add_item_to_cart, 
    remove_item_from_cart, 
    finish_transaction, 
    generate_bill
)

def inventory_menu() -> None:
    """Show the inventory entry flow."""
    while True:
        print_inventory_menu()
        item_name = input("Enter item name: ")
        item_description = input("Enter item description: ")
        item_price = float(input("Enter item price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        add_item(item_name, item_description, item_price, stock_quantity)
        user_choice = input("Add another item? Enter Y for yes and N for no: ")
        if user_choice.lower() == 'n':
            print_inventory_menu()
            break



def sale_menu() -> None:
    """Show the sales and billing flow."""
    while True:
        print_sales_menu()
        selected_item_id = int(input("Enter item id: "))
        sale_quantity = int(input("Enter item quantity: "))
        add_item_to_cart(selected_item_id, sale_quantity)
        user_choice = input("Add another sale item? Enter Y for yes and N for no: ")
        if user_choice.lower() == 'n':
            bill_total = generate_bill()
            print(f"Total bill amount is {bill_total}")
            input("Press Enter to confirm payment.")
            finish_transaction()
            break
        


def main_menu() -> None:
    """Display the main menu to the user.
    
    return: None
    """
    while True:
        print("===== STORE POS =====", end="\n\n")
        print("1. Sale")
        print("2. Inventory")
        print("3. Exit", end="\n\n")
        menu_option = input("Choose an option: ")
        if menu_option.isnumeric():
            if menu_option == "1":
                print("Opening Sale")
                sale_menu()
            elif menu_option == "2":
                print("Opening Inventory")
                inventory_menu()
            elif menu_option == "3":
                print("Thank you. Goodbye")
                break
            else:
                print("Please choose a valid option")
        else:
            print("Please enter a number from the menu")


if __name__ == "__main__":
    main_menu()
