# cli.py

from inventory import inventory
from openfoodfacts import fetch_product_by_barcode


def view_inventory():
    print("\n📦 Inventory:\n")

    for item in inventory:

        warning = "⚠️ LOW STOCK" if item["stock"] < 5 else ""

        print(
            f"""
ID: {item['id']}
Name: {item['name']}
Brand: {item['brand']}
Price: ${item['price']}
Stock: {item['stock']}
Barcode: {item['barcode']}
{warning}
------------------------
"""
        )


def add_item():
    print("\n➕ Add New Item\n")

    name = input("Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    barcode = input("Barcode: ")

    new_item = {
        "id": len(inventory) + 1,
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock,
        "barcode": barcode
    }

    inventory.append(new_item)

    print("\n✅ Item added successfully!")


def search_barcode():
    barcode = input("\n🔎 Enter barcode: ")

    product = fetch_product_by_barcode(barcode)

    if "error" in product:
        print("\n❌ Product not found")
        return

    print(
        f"""
📦 Product Found

Name: {product['name']}
Brand: {product['brand']}
Ingredients:
{product['ingredients']}
"""
    )


def delete_item():
    item_id = int(input("\n🗑️ Enter item ID to delete: "))

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            print("\n✅ Item deleted")
            return

    print("\n❌ Item not found")


def menu():

    while True:

        print(
            """
========================
📦 Inventory Manager
========================

1. View Inventory
2. Add Item
3. Search Barcode
4. Delete Item
5. Exit
"""
        )

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_item()

        elif choice == "3":
            search_barcode()

        elif choice == "4":
            delete_item()

        elif choice == "5":
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Invalid choice")


if __name__ == "__main__":
    menu()