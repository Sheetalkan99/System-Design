from abc import ABC, abstractmethod

class promotion_startegy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class NoDiscount(promotion_startegy):
    def apply_discount(self, total: float) -> float:
        return total

class FlatDiscount(promotion_startegy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

class PercentageDiscount(promotion_startegy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percent / 100)
