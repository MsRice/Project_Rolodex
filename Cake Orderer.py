import time

cake_menu = {
    "chocolate cake": 15.99,
    "vanilla cake": 12.99,
    "Strwaberry cake": 14.99,
    "red velvet cake": 18.99,
    "cheesecake": 16.99
}

def display_menu():
    print("Availible Cakes:")
    for cake ,price in cake_menu.items():
        print(f"- {cake.title()}: ${price:.2f}")

def order_cake():
    choice = input("Enter the cake name:").lower()

    if choice in cake_menu:
        quantity = int(input("Enter quantity:"))
        total_price =  cake_menu[choice] * quantity

        print(f"You ordered {quantity} X {choice.title()} for a total of ${total_price:.2f}.")
        simulate_baking()

    else:
        print("Sorry, that cake is not available")

def simulate_baking():
    print("Baking your cake...")
    time.sleep(4)
    print('Decorating your ckae...')
    time.sleep(2)
    print("Your cake is ready! Enjoy!")

def main():
    print('-' * 30)
    print("1. Show Cake Menu")
    print("2. Order a Cake")
    print("3. Exit")


    choice =  input("Enter your choice (1-3): ")
    print('-' * 30)

    if choice == "1":
        display_menu()
    elif choice == "2":
        order_cake()
    elif choice =="3":
        print("Thank you for visiting! Have a sweet day!")

    else:
        print("Invalid choice! Please enter a number between 1-3.")


if __name__ == "__main__":
    main()
