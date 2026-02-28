import pytest
from quick_calc.calc import add, sub, mul, div, clear

def test_add():
    assert add(5, 3) == 8

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(6, 7) == 42

def test_div():
    assert div(8, 2) == 4

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)

def test_negative():
    assert add(-2, -3) == -5

def test_decimal():
    assert div(1, 2) == 0.5

def test_clear():
    assert clear() == 0