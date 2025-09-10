# from size import Size
# from topping import Topping
# from margherita import margherita

# pizza = margherita(Size.medium)
# pizza.add_toppings(Topping("Cheese", 1.0))
# pizza.add_toppings(Topping("Olives", 0.5))

# print(pizza.get_description())
# print(pizza.get_cost())


#Testing Pizza Factory CLass
from pizza_factory import PizzaFactory
from size import Size

pizza1 = PizzaFactory.create_pizza("margherita", Size.medium)
print(pizza1.get_description())
print(pizza1.get_cost())