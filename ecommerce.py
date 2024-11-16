products = [{"name": "Laptop", "price": 1000}, {"name": "Smartphone", "price": 500}]
cart = []

def view_products():
    print("Available Products:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} - ${product['price']}")

def add_to_cart():
    view_products()
    product_id = int(input("Enter product number to add to cart: "))
    if 1 <= product_id <= len(products):
        cart.append(products[product_id - 1])
        print("Product added to cart!")
    else:
        print("Invalid product number.")

def view_cart():
    print("Cart Items:")
    total = 0
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} - ${item['price']}")
        total += item['price']
    print(f"Total: ${total}")

def main():
    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            view_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

main()