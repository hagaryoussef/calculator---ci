import pytest
from calculator import Calculator

c = Calculator()

def test_add_positive():
    assert c.add(2, 3) == 5

def test_add_negative():
    assert c.add(-2, -3) == -5

def test_add_zero():
    assert c.add(5, 0) == 5

def test_subtract_positive():
    assert c.subtract(5, 3) == 2

def test_subtract_negative():
    assert c.subtract(-5, -3) == -2

def test_subtract_zero():
    assert c.subtract(5, 0) == 5

def test_multiply_positive():
    assert c.multiply(2, 3) == 6

def test_multiply_negative():
    assert c.multiply(-2, 3) == -6

def test_multiply_zero():
    assert c.multiply(5, 0) == 0

def test_divide_normal():
    assert c.divide(6, 3) == 2

def test_divide_float():
    assert c.divide(1, 2) == 0.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        c.divide(1, 0)