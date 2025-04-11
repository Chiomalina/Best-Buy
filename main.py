from random import choice

import products
import store


def start_store(store_instance):
    menu_list = ("""
    Store Menu
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit""")
    print(menu_list)

    while True:
        user_choice = input("\nPlease choose a number (1-4):\n")


        try:
            # Convert user input to integer
            user_choice = int(user_choice)

            # Check if it's in the valid range
            if 1 < user_choice > 4:
                # Raise ValueError if outside the expected range
                raise ValueError("Choice must be a number between 1 and 4.")
        except Exception as e:
            print(f"Invalid input: {e}")
            continue

        if user_choice == 1:
            # 1. List all active products
            all_products = store_instance.get_all_products()
            if not all_products:
                print("No active product in the store.")
            else:
                #print("Active products in the store:")
                print("-" * 6)
                for product in all_products:
                    print(f"{product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")
                print("-" * 6)
                print(menu_list)

        elif user_choice == 2:
            # 2. Show total amount (quantity) in store
            total = store_instance.get_total_quantity()
            print(f"Total of {total} items in store. ")
            print(menu_list)

        elif user_choice == 3:
            # 3. Make an order
            all_products = store_instance.get_all_products()
            if not all_products:
                print("No active product in the store.")
            else:
                print("Active products in the store:")
                print("-" * 20)
                for index, product in enumerate(all_products, start=1):
                    print(f"{index}. {product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")
                print("-" * 20)
                # for product in all_products:
                #     print(f"{product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")

                shopping_list = []

                while True:
                    user_input = input("Which product do you want? (Enter empty text to finish)\n")

                    # If user enters empty text, break out of the loop
                    # if not product_number:
                    #     break
                    if  not user_input or user_input.lower() == "empty":
                        break

                    try:
	                    # Only convert user_input to int if it's not empty
                        product_index = int(user_input) -1
                        chosen_product = all_products[product_index]
                    except ValueError:
                        print("Invalid product number. Please try again.")
                    except IndexError:
                        print("Invalid product number. Please try again")
                        continue


                    quantity_str = input(f"What amount do you want?\n")
                    try:
                        quantity = int(quantity_str)
                    except ValueError:
                        print("Quantity must be a number. Please try again.")
                        continue

                    # Add the chosen product and quantity to the shopping list
                    shopping_list.append((chosen_product, quantity))
                    print(f"Product added to list: {chosen_product.name} (x{quantity})")

                # Now that the user is done adding products, let's buy them
                if shopping_list:
                    total_cost = store_instance.order(shopping_list)
                    print(f"Order complete! Total cost: ${total_cost:.2f}")
                else:
                    print("No products were selected for this order.")
                print(menu_list)


        elif user_choice == 4:
            # 4. Quit
            print("Existing....\nProgram ended")
            break

        else:
            print("Invalid choice! Please chose a number between 1 and 4.")





if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start_store(best_buy)




