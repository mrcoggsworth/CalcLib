"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 0 == calculator.subtract(2, 2)

    def test_multiply(self):
        assert 25 == calculator.multiply(5, 5)

    def test_divide(self):
        assert 5 == calculator.divide(25, 5)
