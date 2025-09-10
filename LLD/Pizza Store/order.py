class Order:
    def __init__(self):
        self.pizza = []

    def add_pizza(self,pizza):
        self.pizza.append(pizza)
    
    def show_order(self):
        print("Your Pizza Order:")
        for i, pizza in enumerate(self.pizza, start = 1):
            print(f"{i}.{pizza.get_description()}")
            if pizza.toppings:
                print(" Toppings ")
                for toppings in pizza.toppings:
                    print(f"   -{toppings}")
            print(f"   Cost: ${pizza.get_cost():.2f}")
    
    def get_total_cost(self):
        return sum(pizza.get_cost() for pizza in self.pizza)