items = []

def add_item(name: str, quantity:int = 1, price:int = 0):
    items.append({
        "name": name, "quantity": quantity, "price": price
    })

def remove_item(name: str):
    for index in range(len(items)):
        item = items[index]
        if item["name"] == name:
            items.pop(index)
            break

def view_cart():

    if len(items) == 0:
        print("Cart is Empty")
        return
    
    for item in items:
        print(f"{item["name"]} - {item["quantity"]} qty -  Rs {item["price"]}")

def calculate_total():
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]

    print("Total price is Rs : ", total)


def checkout():
    calculate_total()
    print("=== Thank for shopping ===")

while True:
    try:

        print("== Welcome to Shopping ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Check Total Price")
        print("5. Checkout")
        print()
        print()

        choice = int(input("Choose Option between 1 to 5"))

        if choice == 1:
            name = input("Enter product name")
            quantity = int(input("Enter product Quantity"))
            price = int(input("Enter product price"))
            add_item(name,quantity,price)
        elif choice == 2:
            name = input("Enter product name to remove")
            remove_item(name)
        elif choice == 3:
            view_cart()
        elif choice == 4:
            calculate_total()

        elif choice == 5:
            checkout()
            break
        else:
            print("Enter valid number between 1 to 5")

    except ValueError:
        print("Error: Please enter a valid choice between 1 to 5")


