# Initial inventory
inventory = [
    {'name': 'Laptop', 'price': 50000, 'quantity': 5}
]

def add_product():
    name = input("Enter product name: ")

    # Prevent duplicate product names
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("❌ Product already exists.")
            return

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        # Ensure positive values
        if price <= 0 or quantity <= 0:
            print("❌ Price and quantity must be positive.")
            return

        inventory.append({'name': name, 'price': price, 'quantity': quantity})
        print(f"✅ Product '{name}' added successfully.")

    except ValueError:
        print("❌ Invalid input. Price and quantity must be numbers.")

def view_products():
    if not inventory:
        print("📦 Inventory is empty.")
        return

    print("\nName\t\tPrice\t\tQuantity")
    print("-" * 40)
    for product in inventory: