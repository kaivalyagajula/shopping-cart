
import datetime

# store inventory
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

# create empty shopping cart and quantity list
shopping_cart = []
quantities = []

choice = 0

# menu until checkout is completed
while choice != 6:
    print("========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()

    choice = int(input("Enter your choice: "))
    print()

    # validate the main menu choice
    while choice < 1 or choice > 6:
        print("Invalid option!")
        choice = int(input("Choose a number between 1 and 6: "))
        print()

    # view available products
    if choice == 1:
        print("========== AVAILABLE PRODUCTS ==========")

        index = 0
        for product in products:
            price = prices[index]
            print(index + 1, ".", product, "- $" + str(price))
            index += 1

        print()

    # add a product
    elif choice == 2:
        print("========== AVAILABLE PRODUCTS ==========")

        index = 0
        for product in products:
            print(index + 1, ".", product)
            index += 1

        product_num = int(input("Enter product number: "))

        # validate product number
        while product_num < 1 or product_num > len(products):
            print("Invalid product!")
            product_num = int(input("Choose a number between 1 and 6: "))

        chosen_product = products[product_num - 1]

        # check whether product is already in the cart
        if chosen_product in shopping_cart:
            cart_index = shopping_cart.index(chosen_product)
            quantities[cart_index] += 1
            print(chosen_product, "quantity increased to",
                  quantities[cart_index], "!")
        else:
            shopping_cart.append(chosen_product)
            quantities.append(1)
            print(chosen_product, "was added to your cart!")

        print()

    # remove product from the cart
    elif choice == 3:
        print("========== YOUR SHOPPING CART ==========")

        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
            print("There is nothing to remove.")
        else:
            index = 0
            for product in shopping_cart:
                print(index + 1, ".", product,
                      "- Quantity:", quantities[index])
                index += 1

            remove_num = int(input("Which product would you like to remove? "))

            # validate removal
            while remove_num < 1 or remove_num > len(shopping_cart):
                print("That item does not exist in your cart!")
                remove_num = int(input("Enter a valid item number: "))

            cart_index = remove_num - 1
            removed_product = shopping_cart[cart_index]

            # decrease quantity if more than one item exists
            if quantities[cart_index] > 1:
                quantities[cart_index] -= 1
                print("One", removed_product, "was removed!")
                print(removed_product, "quantity is now",
                      quantities[cart_index], ".")
            else:
                shopping_cart.pop(cart_index)
                quantities.pop(cart_index)
                print(removed_product, "was removed from your cart!")

        print()

    # view the shopping cart
    elif choice == 4:
        print("========== YOUR SHOPPING CART ==========")

        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
        else:
            total_items = 0
            subtotal = 0

            print("Product       Price     Quantity     Total")

            for index in range(len(shopping_cart)):
                product = shopping_cart[index]
                quantity = quantities[index]

                product_index = products.index(product)
                price = prices[product_index]
                item_total = price * quantity

                print(str(index + 1) + ". " + product +
                      "       $" + str(price) +
                      "        " + str(quantity) +
                      "          $" + str(item_total))

                total_items += quantity
                subtotal += item_total

            print()
            print("Total Items:", total_items)
            print("Subtotal: $" + str(subtotal))

        print()

    # view the current subtotal
    elif choice == 5:
        print("========== CURRENT TOTAL ==========")

        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
        else:
            subtotal = 0

            for index in range(len(shopping_cart)):
                product = shopping_cart[index]
                quantity = quantities[index]

                product_index = products.index(product)
                price = prices[product_index]
                item_total = price * quantity

                print(product, "x", quantity, "- $" + str(item_total))

                subtotal += item_total

            print()
            print("Subtotal: $" + str(subtotal))

        print()

    # checkout and print the receipt
    elif choice == 6:
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty!")
            print("Add a product before checking out.")
            choice = 0
            print()
        else:
            subtotal = 0

            # calculate the subtotal using product quantities
            for index in range(len(shopping_cart)):
                product = shopping_cart[index]
                product_index = products.index(product)
                price = prices[product_index]

                subtotal += price * quantities[index]

            # determine the discount
            if subtotal < 10:
                discount_rate = 0
            elif subtotal < 20:
                discount_rate = 0.05
            elif subtotal < 40:
                discount_rate = 0.10
            else:
                discount_rate = 0.15

            amount_saved = subtotal * discount_rate
            final_total = subtotal - amount_saved

            # get current date using the datetime module
            current_date = datetime.date.today()

            print("========== RECEIPT ==========")
            print("Date:", current_date.strftime("%m/%d/%Y"))
            print()

            for index in range(len(shopping_cart)):
                product = shopping_cart[index]
                product_index = products.index(product)
                price = prices[product_index]
                quantity = quantities[index]
                item_total = price * quantity

                print(product, "x", quantity,
                      "- $" + str(item_total))

            print()
            print("Subtotal:       $" + str(subtotal))
            print("Discount:       " + str(discount_rate * 100) + "%")
            print("Amount Saved:   $" + str(amount_saved))
            print("Final Total:    $" + str(final_total))
            print()
            print("Thank you for shopping!")
            print()
