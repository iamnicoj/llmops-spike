import pytest
from apps.geometry.circle import Circle


def test_area():
    # Test case 1: Testing area calculation for a circle with radius 4
    circle = Circle(4)
    assert circle.get_area() == pytest.approx(50.26548, rel=1e-5)

    # Test case 2: Testing area calculation for a circle with radius 7
    circle = Circle(7)
    assert circle.get_area() == pytest.approx(153.93804, rel=1e-5)

    # Test case 3: Testing area calculation for a circle with radius 10
    circle = Circle(10)
    assert circle.get_area() == pytest.approx(314.15926, rel=1e-5)


def test_circumference():
    # Test case 1: Testing circumference calculation for a circle with radius 4
    circle = Circle(4)
    assert circle.get_circumference() == pytest.approx(25.13274, rel=1e-5)

    # Test case 2: Testing circumference calculation for a circle with radius 7
    circle = Circle(7)
    assert circle.get_circumference() == pytest.approx(43.9823, rel=1e-5)

    # Test case 3: Testing circumference calculation for a circle with radius 10
    circle = Circle(10)
    assert circle.get_circumference() == pytest.approx(62.83185, rel=1e-5)
