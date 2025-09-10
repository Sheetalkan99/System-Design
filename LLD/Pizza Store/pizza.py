from abc import ABC, abstractmethod
from size import Size

class pizza(ABC):
    def __init__(self,size: Size):
        self.size = size
        self.toppings = []
    def add_toppings(self, topping):
        self.toppings.append(topping)

    @abstractmethod 
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass