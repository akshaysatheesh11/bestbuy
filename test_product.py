import pytest
from your_module_name import Product  # Replace 'your_module_name' with the actual module name where Product is defined.

def test_create_normal_product():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active is True

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name should raise an exception
    
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price should raise an exception

def test_product_becomes_inactive_when_quantity_zero():
    product = Product(name="MacBook Air M2", price=1450, quantity=1)
    product.purchase(1)  # Reduces quantity to 0
    assert product.quantity == 0
    assert product.is_active is False

def test_product_purchase_modifies_quantity():
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    cost = product.purchase(10)  # Purchase 10 items
    assert product.quantity == 90  # Quantity should decrease
    assert cost == 14500  # Cost should be 1450 * 10

def test_purchase_more_than_available_quantity():
    product = Product(name="MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError):
        product.purchase(20)  # Trying to purchase more than available should raise an exception
