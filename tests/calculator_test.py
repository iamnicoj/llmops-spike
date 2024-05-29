import pytest
from apps.calculator.calculator import Calculator


def test_addition():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5


def test_subtraction():
    calc = Calculator()
    result = calc.subtract(5, 3)
    assert result == 2


def test_multiplication():
    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20


def test_division():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5

# Test case for division by zero: expected to fail


def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
