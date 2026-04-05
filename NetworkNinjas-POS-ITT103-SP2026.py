# Welcome message displayed when the program starts
print("Welcome to Best Buy, try something new today")

# Ask for cashier name once when the system starts
# We use .strip() to remove accidental whitespace at the start or end.
cashier_name = input("Please enter your name: ").strip()

# Validate cashier name
if cashier_name.replace(" ", "").isalpha() and cashier_name != "":
    print("\nHello,", cashier_name + "! Let's start your transaction.\n")
else:
    print("Invalid name. Cashier set as 'Staff'.")
    cashier_name = "Staff"


def main():

    # Product dictionary storing price and stock in Best Buy Retail
    products = {
        "Egg": {"price": 950.00, "stock": 12},
        "Sausage": {"price": 550.00, "stock": 18},
        "Chicken": {"price": 1300.00, "stock": 25},
        "Cheese": {"price": 700.00, "stock": 10},
        "Sugar": {"price": 650.00, "stock": 15},
        "Rice": {"price": 700.00, "stock": 21},
        "Water": {"price": 300.00, "stock": 3},
        "Oil": {"price": 1500.00, "stock": 28},
        "Bread": {"price": 750.00, "stock": 20},
        "Butter": {"price": 500.00, "stock": 12}
    }

    running = True

    while running:

        # 'shopping_cart' is reset for every new customer to ensure data privacy.
        # Key: Product Name, Value: Quantity purchased.
        # Ask for customer name at the start of each transaction for a personal experience
        cust_name = input("\nEnter customer's name: ").strip()

        if not cust_name.replace(" ", "").isalpha() or cust_name == "":
            print("Invalid name. Using 'Customer'.")
            cust_name = "Customer"

        print("\nNow serving:", cust_name)

        # New cart for each customer at the start of each transaction
        shopping_cart = {}
        # # 'menu_active' controls the individual Customer Session
        menu_active = True

        while menu_active:
            print("\n BEST BUY RETAIL POS MENU ")
            print("1. View Product Catalog")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit System")

            choice = input("Select an option (1-6): ").strip()

            # This section displays the products and the section that controls the products stock and price
            if choice == "1":
                print("\nPRODUCTS AVAILABLE:")
                print("Item\t\tPrice\t\tStock")

                for item in products:
                    price = products[item]["price"]
                    stock = products[item]["stock"]

                    if stock < 5:
                        print(item, "$" + str(price), stock, "(LOW STOCK!)")
                    else:
                        print(item, "$" + str(price), stock)

            # Adds selected items to the customers cart
            elif choice == "2":
                while True:
                    item_name = input("Enter product name: ").strip().capitalize()

                    if item_name in products:
                        break
                    else:
                        print("Product not found.")
                        print("Available:", ", ".join(products.keys()))

                qty_input = input("Enter quantity: ")

                if qty_input.isdigit():
                    qty = int(qty_input)

                    if qty > 0 and qty <= products[item_name]["stock"]:
                        shopping_cart[item_name] = shopping_cart.get(item_name, 0) + qty
                        products[item_name]["stock"] -= qty
                        print(item_name, "added to cart.")
                    else:
                        print("Invalid quantity or insufficient stock.")
                else:
                    print("Enter a valid number.")

            # Removes items from cart and transaction
            elif choice == "3":
                if not shopping_cart:
                    print("Cart is empty.")
                else:
                    print("Cart items:", ", ".join(shopping_cart.keys()))
                    rem = input("Enter item to remove: ").strip().capitalize()

                    if rem in shopping_cart:
                        products[rem]["stock"] += shopping_cart[rem]
                        del shopping_cart[rem]
                        print(rem, "removed.")
                    else:
                        print("Item not in cart.")

            # View cart
            elif choice == "4":
                if not shopping_cart:
                    print("Cart is empty.")
                else:
                    total = 0
                    for item in shopping_cart:
                        qty = shopping_cart[item]
                        price = products[item]["price"]
                        item_total = qty * price
                        total += item_total
                        print(item, qty, "x", price, "=", item_total)

                    print("Cart Total:", total)

            # Checkout
            elif choice == "5":
                if not shopping_cart:
                    print("Cart empty.")
                else:
                    subtotal = sum(shopping_cart[i] * products[i]["price"] for i in shopping_cart)

                    discount = subtotal * 0.05 if subtotal > 5000 else 0
                    tax = (subtotal - discount) * 0.10
                    total = (subtotal - discount) + tax

                    print("\nSubtotal:", subtotal)
                    if discount > 0:
                        print("Discount:", discount)
                    print("Tax:", tax)
                    print("TOTAL:", total)

                    while True:
                        try:
                            paid = float(input("Enter payment: "))

                            if paid >= total:
                                change = paid - total

                                # Receipt generation
                                print("\n" + "*" * 40)
                                print("Best Buy Retail Store,Try Something New Everyday!")
                                print("*" * 40)
                                print("Cashier:", cashier_name)
                                print("Customer Served:", cust_name)
                                print("-" * 40)

                                for item in shopping_cart:
                                    print(item, "x", shopping_cart[item])

                                print("-" * 40)
                                print("TOTAL:", total)
                                print("Paid:", paid)
                                print("Change:", change)
                                print("*" * 40)
                        

                                break
                            else:
                                print("Insufficient payment.")
                        except ValueError:
                            print("Invalid input.")

                    # complete the transaction and ask for a new customer
                    print("\n*******Thank you Shopping with us at Best Buy!*****24 Constant Spring Mall**** ")

                    next_cust = input("\nProcess another customer? (yes/no): ").strip().lower()

                    if next_cust != "yes":
                        print("System Closed.")
                        running = False

                    menu_active = False

            # Exit system
            elif choice == "6":
                print("System shutting down...")
                running = False
                menu_active = False

            else:
                print("Invalid option.")



main()