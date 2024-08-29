# File: products.py

from abc import ABC, abstractmethod

# Promotion abstract class and concrete implementations
class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        discount = self.percent / 100
        return product.price * quantity * (1 - discount)

class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)

class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        groups_of_three = quantity // 3
        full_price_items = quantity - groups_of_three
        return full_price_items * product.price


# Product class and its subclasses
class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid parameters provided for product creation.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True
        self.promotion = None  # Add promotion attribute

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

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def show(self):
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")
        
        if self.promotion:
            total_cost = self.promotion.apply_promotion(self, quantity)
        else:
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
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} (Non-Stocked){promotion_info}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} units of this product.")
        return super().buy(quantity)

    def show(self):
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Max per order: {self.maximum}{promotion_info}"
