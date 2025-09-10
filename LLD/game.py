class product:
    def __init__(self,id,name, price,quanity):
        self.id = id
        self.name = name 
        self.price = price 
        self.quanity = quanity 

class Discount:
    def __init__(self):
        self.codes = {
            "SAVE10" : 10,
            "SAVE20" : 20
        }
    def add_discount_code(self,code,num):
        if code not in self.codes:
            self.codes[code] = num
        else:
            print(f"Already in codes")
    def get_discount(self,code):
        return self.codes.get(code.upper(),0)




class shopping_cart:
    def __init__(self):
        self.cart = {}

    def add_item(self,product:product):
        
        if product.id in self.cart:
            name, price, qty = self.cart[product.id]
            self.cart[product.id] = name,price, qty + 1
        else:
            self.cart[product.id] = [product.name,product.price,product.quanity]

    def display_cart(self):
        if self.cart is None:
            print("No item in Cart!")
        else:
            for id, (name,price,qty) in self.cart.items():
                print(f"Name:{name}, Price : {price}, qty: {qty}")
        total,distotal = self.calculate_total()
        print(f"Total:{total}")
        print(f"Total After Discount: {distotal}")
            
    def calculate_total(self):
        total = 0
        if self.cart is None:
            print("No item in Cart!")
        else:
            for id, (name,price,qty) in self.cart.items():
                total += price * qty
        distotal = total
        if self.discount_percentage > 0:
                distotal -= total * (self.discount_percentage / 100)
        return total,distotal
    
    def apply_discount(self,discount : Discount, code:str):
        self.discount_percentage = discount.get_discount(code)
        if self.discount_percentage > 0:
            print(f"Discount code applied: {self.discount_percentage}% off")
        else:
            print("Invalid discount code.")
    
    def remove_item(self,id,rqty = 1):
        if id in self.cart:
            name,price,qty = self.cart[id]
            if qty > rqty:
                self.cart[id] = [name,price, qty - rqty]
            else:
                del self.cart[id]



p1 = product(101,"Laptop",1200,1)
p2 = product(101,"Laptop",1200,1)
p3 = product(102," Apple", 200,1)
cart = shopping_cart()
cart.add_item(p1)
cart.add_item(p2)
cart.add_item(p3)
cart.remove_item(p1.id,1)
discount_handler = Discount()
cart.apply_discount(discount_handler, "SAVE20")

cart.display_cart()

        
    
