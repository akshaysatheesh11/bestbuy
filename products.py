# File: products.py

class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid parameters provided for product creation.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        
        total_cost = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_cost
