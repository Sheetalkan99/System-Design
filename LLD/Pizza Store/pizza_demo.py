from size import Size
from topping import Topping 
from pizza_factory import PizzaFactory
from order import Order
from bill import Bill
from promotion import FlatDiscount, PercentageDiscount

order = Order()

pizza1 = PizzaFactory.create_pizza("margherita", Size.small)
pizza1.add_toppings(Topping("Cheese",1.0))

pizza2 = PizzaFactory.create_pizza("framhouse",Size.medium)
pizza2.add_toppings(Topping("Mushroom", 0.75))

order.add_pizza(pizza1)
order.add_pizza(pizza2)

promo = PercentageDiscount(10)

bill = Bill(order,promo)
bill.print_bill()