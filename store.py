# File: store.py
from typing import List
import products

class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity

    def get_all_products(self) -> List[products.Product]:
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list):
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
