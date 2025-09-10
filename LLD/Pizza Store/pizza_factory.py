from margherita import margherita
from farmhouse import farmhouse
from size import Size

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type : str, size : Size):
        pizza_type = pizza_type.lower()

        if pizza_type == "margherita":
            return margherita(size)
        elif pizza_type == "framhouse":
            return farmhouse(size)
        else:
            raise ValueError(f"{pizza_type} is Unknown.")