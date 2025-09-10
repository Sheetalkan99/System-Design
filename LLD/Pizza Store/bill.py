from promotion import promotion_startegy

class Bill:
    def __init__(self,order,promo: promotion_startegy):
        self.order = order
        self.promo = promo

    def print_bill(self):

        print("\n ------ FINAL BILL -------")
        self.order.show_order()

        raw_total = self.order.get_total_cost()
        discounted_total = self.promo.apply_discount(raw_total)


        print(f"\n Subtotal : ${raw_total: .2f}")
        print(f"Discounted Total: ${discounted_total:.2f}")