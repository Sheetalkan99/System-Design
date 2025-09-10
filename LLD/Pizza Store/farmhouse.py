from size import Size
from pizza import pizza

class farmhouse(pizza):
    def get_description(self):
        return f"Farmhouse Pizza ({self.size.name})"
    def get_cost(self):
        base_price = {
            Size.small: 5,
            Size.medium: 7,
            Size.large: 9
        }

        topping_cost = sum(t.price for t in self.toppings)
        return base_price[self.size] + topping_cost