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


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.activate()  # Always active since quantity is irrelevant

    def set_quantity(self, quantity):
        # Override to prevent setting quantity
        pass

    def buy(self, quantity):
        # Non-stocked products don't track quantity
        return self.price * quantity

    def show(self):
        return f"{self.name}, Price: ${self.price} (Non-Stocked)"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of this product.")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}"
