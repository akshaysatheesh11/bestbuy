# File: main.py
import products
import store

def start(store_obj):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == '1':
            print("------")
            products_in_store = store_obj.get_all_products()
            for i, product in enumerate(products_in_store, 1):
                print(f"{i}. {product.show()}")
            print("------")

        elif choice == '2':
            total_quantity = store_obj.get_total_quantity()
            print(f"Total of {total_quantity} items in store")

        elif choice == '3':
            shopping_list = []
            print("------")
            products_in_store = store_obj.get_all_products()
            for i, product in enumerate(products_in_store, 1):
                print(f"{i}. {product.show()}")
            print("------")
            print("When you want to finish order, enter empty text.")

            while True:
                product_number = input("Which product # do you want? ")
                if not product_number:
                    break
                try:
                    product_number = int(product_number)
                    if 1 <= product_number <= len(products_in_store):
                        product = products_in_store[product_number - 1]
                        quantity = int(input(f"Enter quantity for '{product.name}': "))
                        shopping_list.append((product, quantity))
                    else:
                        print(f"Product number {product_number} is not valid.")
                except ValueError:
                    print("Please enter a valid product number or leave blank to finish.")

            try:
                order_cost = store_obj.order(shopping_list)
                print(f"Order cost: ${order_cost} dollars.")
            except Exception as e:
                print(e)

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
