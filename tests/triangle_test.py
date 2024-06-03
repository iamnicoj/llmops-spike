import pytest
from apps.geometry.triangle import Triangle


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_area() == 6


def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_perimeter() == 12


def test_triangle_right_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_triangle() == True


def test_triangle_invalid_side_lengths():
    with pytest.raises(ValueError):
        Triangle(1, 2, 10)


def test_triangle_invalid_negative_side_lengths():
    with pytest.raises(ValueError):
        Triangle(-3, 4, 5)
