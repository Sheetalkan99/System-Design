from size import Size
from topping import Topping
from pizza_factory import PizzaFactory
from order import Order
from bill import Bill
from promotion import FlatDiscount, PercentageDiscount, NoDiscount

def choose_size():
    print("Choose Size:")
    print("1. Small\n2. Medium\n3. Large")
    choice = input("Enter choice (1-3): ")
    return {
        "1": Size.small,
        "2": Size.medium,
        "3": Size.large
    }.get(choice, Size.medium) 

def add_toppings():
    toppings = []
    while True:
        name = input("Enter topping name (or press Enter to stop): ")
        if not name:
            break
        try:
            price = float(input(f"Enter price for {name}: "))
        except ValueError:
            print("Invalid price. Try again.")
            continue
        toppings.append(Topping(name, price)) 
    return toppings 

def choose_promotion():
    print("\nChoose Promotion:")
    print("1. Flat Discount ($5 off)")
    print("2. Percentage Discount (10%)")
    print("3. No Discount")

    promo_choice = input("Enter choice (1-3): ")
    if promo_choice == "1":
        return FlatDiscount(5)
    elif promo_choice == "2":
        return PercentageDiscount(10)
    else:
        return NoDiscount()  # FIXED: You missed the () to instantiate the class

def main():
    order = Order()
    print("Welcome to the Pizza Pizza Store!\n")
    
    while True:
        pizza_type = input("Enter pizza type (Margherita / Farmhouse): ").strip().lower()
        size = choose_size()

        try:
            pizza = PizzaFactory.create_pizza(pizza_type, size)
        except ValueError as e:
            print(e)
            continue

        toppings = add_toppings()
        for t in toppings:
            pizza.add_toppings(t)

        order.add_pizza(pizza)

        more = input("Add another pizza? (y/n): ").strip().lower()
        if more != 'y':
            break

    promo = choose_promotion()
    bill = Bill(order, promo)
    bill.print_bill() 

if __name__ == "__main__":
    main()
