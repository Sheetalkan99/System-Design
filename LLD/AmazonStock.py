from abc import ABC, abstractmethod

# ----------------------------
# AlertPolicy Interface (Strategy)
# ----------------------------
class AlertPolicy(ABC):
    @abstractmethod
    def should_alert(self, current_stock: int) -> bool:
        pass

# Concrete: Fixed threshold
class FixedThresholdPolicy(AlertPolicy):
    def __init__(self, threshold: int):
        self.threshold = threshold

    def should_alert(self, current_stock: int) -> bool:
        return current_stock < self.threshold

# Concrete: Percentage-based threshold
class PercentageThresholdPolicy(AlertPolicy):
    def __init__(self, max_capacity: int, percentage: float):
        self.max_capacity = max_capacity
        self.percentage = percentage  # e.g., 0.1 means 10%

    def should_alert(self, current_stock: int) -> bool:
        return current_stock < self.max_capacity * self.percentage

# ----------------------------
# AlertListener Interface (Observer)
# ----------------------------
class AlertListener(ABC):
    @abstractmethod
    def notify(self, product_id: str, fc_id: str, stock: int):
        pass

# Concrete: Just print alert
class PrintAlertListener(AlertListener):
    def notify(self, product_id: str, fc_id: str, stock: int):
        print(f"[ALERT] Low stock for {product_id} in {fc_id}! Current stock = {stock}")

# ----------------------------
# ProductStock Class
# ----------------------------
class ProductStock:
    def __init__(self, product_id: str, fc_id: str,
                 policy: AlertPolicy,
                 listener: AlertListener):
        self.product_id = product_id
        self.fc_id = fc_id
        self.policy = policy
        self.listener = listener

        self.current_stock = 0
        self.alert_sent = False

    def decrease_stock(self, qty: int):
        self.current_stock = max(0, self.current_stock - qty)
        if self.policy.should_alert(self.current_stock) and not self.alert_sent:
            self.listener.notify(self.product_id, self.fc_id, self.current_stock)
            self.alert_sent = True

    def restock(self, qty: int):
        self.current_stock += qty
        if not self.policy.should_alert(self.current_stock):
            self.alert_sent = False

    def get_stock(self):
        return self.current_stock

    def clear_alert(self):
        self.alert_sent = False

# ----------------------------
# StockMonitor Class (Manager)
# ----------------------------
class StockMonitor:
    def __init__(self):
        self.inventory = {}  # key: (product_id, fc_id)

    def register_product(self, product_id: str, fc_id: str, threshold: int):
        key = (product_id, fc_id)
        if key not in self.inventory:
            policy = FixedThresholdPolicy(threshold)
            listener = PrintAlertListener()
            self.inventory[key] = ProductStock(product_id, fc_id, policy, listener)

    def register_product_with_percentage_threshold(self, product_id: str, fc_id: str, max_capacity: int, percentage: float):
        key = (product_id, fc_id)
        if key not in self.inventory:
            policy = PercentageThresholdPolicy(max_capacity, percentage)
            listener = PrintAlertListener()
            self.inventory[key] = ProductStock(product_id, fc_id, policy, listener)

    def decrease_stock(self, product_id: str, fc_id: str, qty: int):
        key = (product_id, fc_id)
        if key in self.inventory:
            self.inventory[key].decrease_stock(qty)
        else:
            print(f"[ERROR] Product not registered: {product_id} @ {fc_id}")

    def restock(self, product_id: str, fc_id: str, qty: int):
        key = (product_id, fc_id)
        if key in self.inventory:
            self.inventory[key].restock(qty)
        else:
            print(f"[ERROR] Product not registered: {product_id} @ {fc_id}")

    def get_stock(self, product_id: str, fc_id: str):
        key = (product_id, fc_id)
        if key in self.inventory:
            return self.inventory[key].get_stock()
        return None

    def clear_alert(self, product_id: str, fc_id: str):
        key = (product_id, fc_id)
        if key in self.inventory:
            self.inventory[key].clear_alert()

    def print_inventory(self):
        print("📦 Current Inventory:")
        for key, stock in self.inventory.items():
            print(f"{key}: Stock={stock.get_stock()}")


# ----------------------------
# Example Usage / Test Case
# ----------------------------
if __name__ == "__main__":
    monitor = StockMonitor()

    # Register product with fixed threshold
    monitor.register_product("p123", "FC-SEA", 50)

    # Register another product with percentage threshold
    monitor.register_product_with_percentage_threshold("p999", "FC-NYC", max_capacity=200, percentage=0.2)  # alert below 40

    monitor.restock("p123", "FC-SEA", 100)         # Stock = 100
    monitor.decrease_stock("p123", "FC-SEA", 60)   # Stock = 40 → alert
    monitor.decrease_stock("p123", "FC-SEA", 10)   # Stock = 30 → no new alert
    monitor.restock("p123", "FC-SEA", 30)          # Stock = 60 → reset alert
    monitor.decrease_stock("p123", "FC-SEA", 25)   # Stock = 35 → alert again

    monitor.restock("p999", "FC-NYC", 100)         # Stock = 100 (threshold is 40)
    monitor.decrease_stock("p999", "FC-NYC", 70)   # Stock = 30 → alert

    monitor.print_inventory()
