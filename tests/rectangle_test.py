import pytest
from apps.geometry.rectangle import Rectangle


def test_rectangle_area():
    rectangle = Rectangle(5, 10)
    assert rectangle.get_area() == 50


def test_rectangle_perimeter():
    rectangle = Rectangle(5, 10)
    assert rectangle.get_perimeter() == 30


def test_rectangle_invalid_dimensions():
    with pytest.raises(ValueError) as e:
        Rectangle(5, -10)
    assert str(e.value) == "Length and width must be positive numbers"

    with pytest.raises(ValueError) as e:
        Rectangle(-5, -10)
    assert str(e.value) == "Length and width must be positive numbers"
