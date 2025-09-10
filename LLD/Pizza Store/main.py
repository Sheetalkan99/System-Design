from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal
from size import Size 
from topping import Topping
from pizza_factory import PizzaFactory
from order import Order
from bill import Bill
from promotion import FlatDiscount, PercentageDiscount, NoDiscount

app = FastAPI()

class ToppingInput(BaseModel):
    name: str
    price : float

class PizzaInput(BaseModel):
    pizza_type : Literal["margherita", "farmhouse"]
    size : Size
    toppings: List[ToppingInput] = []

class OrderRequest(BaseModel):
    pizzas: List[PizzaInput]  
    promotion: Literal["flat", "percent", "none"]


@app.post("/order/")
def create_order(order_req: OrderRequest):
    order = Order()

    for pizza_input in order_req.pizza:
        pizza = PizzaFactory.create_pizza(pizza_input.pizza_type,pizza_input.size)
        for t in pizza_input.toppings:
            pizza.add_topping(Topping(t.name,t.price))
        order.add_pizza(pizza)
    
    if order_req.promotion == "flat":
        promo = FlatDiscount(5)
    elif order_req.promotion == "precent":
        promo = PercentageDiscount(10)
    else:
        promo = NoDiscount
    
    bill = Bill(order,promo)
     # Build response
    return {
        "items": [
            {
                "description": pizza.get_description(),
                "toppings": [str(t) for t in pizza.toppings],
                "cost": pizza.get_cost()
            } for pizza in order.pizzas
        ],
        "subtotal": order.get_total_cost(),
        "final_total": promo.apply_discount(order.get_total_cost())
    }
