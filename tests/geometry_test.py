import pytest
from apps.geometry.circle_geometry import CircleGeometry


def test_area():
    # Test case 1: Testing area calculation for a circle with radius 4
    circle = CircleGeometry(4)
    assert circle.get_area() == pytest.approx(50.26548, rel=1e-5)

    # Test case 2: Testing area calculation for a circle with radius 7
    circle = CircleGeometry(7)
    assert circle.get_area() == pytest.approx(153.93804, rel=1e-5)

    # Test case 3: Testing area calculation for a circle with radius 10
    circle = CircleGeometry(10)
    assert circle.get_area() == pytest.approx(314.15926, rel=1e-5)


def test_circumference():
    # Test case 1: Testing circumference calculation for a circle with radius 4
    circle = CircleGeometry(4)
    assert circle.get_circumference() == pytest.approx(25.13274, rel=1e-5)

    # Test case 2: Testing circumference calculation for a circle with radius 7
    circle = CircleGeometry(7)
    assert circle.get_circumference() == pytest.approx(43.9823, rel=1e-5)

    # Test case 3: Testing circumference calculation for a circle with radius 10
    circle = CircleGeometry(10)
    assert circle.get_circumference() == pytest.approx(62.83185, rel=1e-5)
