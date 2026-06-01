import pytest
from my_project.calculator import Calculator


class TestCalculator:
    def test_add(self):
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0

    def test_subtract(self):
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(0, 5) == -5

    def test_multiply(self):
        assert Calculator.multiply(4, 3) == 12
        assert Calculator.multiply(-2, 5) == -10
        assert Calculator.multiply(0, 100) == 0

    def test_divide(self):
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(7, 2) == 3.5

        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            Calculator.divide(5, 0)
