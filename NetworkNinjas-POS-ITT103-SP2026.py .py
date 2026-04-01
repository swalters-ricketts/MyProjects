print("Welcome to Best Buy, try something new today")

name = input("Please enter your name: ").strip()

if name.replace(" ", "").isalpha() and name != "":
    print("\nHello,", name + "! Let's start your transaction.\n")
else:
    print("Invalid name. Please enter letters only.")
    name = input("Enter your name: ").strip()

    if name.replace(" ", "").isalpha() and name != "":
        print("\nHello,", name + "! Let's start your transaction.\n")
    else:
        print("Invalid input again.")


def main():
    products = {
        "Egg":     {"price": 950.00, "stock": 12},
        "Sausage": {"price": 550.00, "stock": 18},
        "Chicken": {"price": 1300.00, "stock": 25},
        "Cheese":  {"price": 700.00, "stock": 10},
        "Sugar":   {"price": 650.00, "stock": 15},
        "Rice":    {"price": 700.00, "stock": 21},
        "Water":   {"price": 300.00, "stock":  3},
        "Oil":     {"price": 1500.00, "stock": 28},
        "Bread":   {"price": 750.00, "stock": 20},
        "Butter":  {"price": 500.00, "stock": 12}
    }
    running = True
    while running:
        shopping_cart = {}

        menu_active = True
        while menu_active:
            print("\n BEST BUY RETAIL POS MENU ")
            print("1. View Product Catalog")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit System")

            choice = input("Select an option from (1-6): ")

            if choice == "1":
                print("\nPRODUCTS AVAILABLE:")
                print("Item\t\tPrice\t\tStock")
                for item in products:
                    p_price = products[item]["price"]
                    p_stock = products[item]["stock"]
                    if p_stock < 5:
                        print(item + "\t\t$" + str(p_price) + "\t\t" + str(p_stock) + " (LOW STOCK!)")
                    else:
                        print(item + "\t\t$" + str(p_price) + "\t\t" + str(p_stock))

            elif choice == "2":
                name = input("Enter product name: ").capitalize()
                if name in products:
                    qty_input = input("Enter quantity: ")
                    if qty_input.isdigit():
                        qty = int(qty_input)
                        if qty <= products[name]["stock"]:
                            if name in shopping_cart:
                                shopping_cart[name] = shopping_cart[name] + qty
                            else:
                                shopping_cart[name] = qty

                            products[name]["stock"] = products[name]["stock"] - qty
                            print(name + " added to cart.")
                        else:
                            print("Sorry, not enough stock. Only " + str(products[name]["stock"]) + " left.")
                    else:
                        print("Invalid quantity. Please enter a number.")
                else:
                    print("Product not found.")

            elif choice == "3":
                rem_name = input("Enter product to remove: ").capitalize()
                if rem_name in shopping_cart:
                    products[rem_name]["stock"] = products[rem_name]["stock"] + shopping_cart[rem_name]
                    del shopping_cart[rem_name]
                    print(rem_name + " removed from cart.")
                else:
                    print("Item not in your cart.")

            elif choice == "4":
                print("\nYOUR CURRENT CART:")
                if not shopping_cart:
                    print("Cart is empty.")
                else:
                    for item in shopping_cart:
                        qty = shopping_cart[item]
                        price = products[item]["price"]
                        item_total = qty * price
                        print(item + ": " + str(qty) + " x $" + str(price) + " = $" + str(item_total))

            elif choice == "5":
                if not shopping_cart:
                    print("Your cart is empty. Nothing to checkout.")
                else:
                    subtotal = 0
                    for item in shopping_cart:
                        qty = shopping_cart[item]
                        price = products[item]["price"]
                        subtotal = subtotal + (qty * price)

                    discount = 0
                    if subtotal > 5000:
                        discount = subtotal * 0.05

                    tax = (subtotal - discount) * 0.10
                    final_total = (subtotal - discount) + tax

                    print("\nSubtotal: $" + str(round(subtotal, 2)))
                    if discount > 0:
                        print("Discount (5%): -$" + str(round(discount, 2)))
                    print("Sales Tax (10%): $" + str(round(tax, 2)))
                    print("TOTAL DUE: $" + str(round(final_total, 2)))

                    payment_made = False
                    while not payment_made:
                        paid_input = input("Enter amount paid by customer: ")
                        try:
                            paid_amount = float(paid_input)
                            if paid_amount >= final_total:
                                change = paid_amount - final_total

                                print("\n" + "*" * 40)
                                print("       BEST BUY RETAIL STORE")
                                print("*" * 40)
                                for item in shopping_cart:
                                    q = shopping_cart[item]
                                    p = products[item]["price"]
                                    t = q * p
                                    print(item + " x" + str(q) + "  Price: $" + str(p) + "  Total: $" + str(t))
                                print("Subtotal: $" + str(round(subtotal, 2)))
                                print("Tax: $" + str(round(tax, 2)))
                                print("TOTAL: $" + str(round(final_total, 2)))
                                print("Paid: $" + str(round(paid_amount, 2)))
                                print("Change: $" + str(round(change, 2)))
                                print(" THANK YOU FOR SHOPPING WITH US!")

                                payment_made = True
                                menu_active = False
                            else:
                                print("Your Payment Is Insufficient! Customer still owes $" + str(
                                    round(final_total - paid_amount, 2)))
                        except:
                            print("Invalid payment amount entered.")
            elif choice == "6":
                print("Exiting POS system. Goodbye and Thank You For Shopping With US!")
                return
        next_cust = input("\nProcess another customer? (yes/no): ").lower()
        if next_cust != "yes":
            running = False
            print("System Closed.")
main()

