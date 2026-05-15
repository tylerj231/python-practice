import pytest

from calculator import Calculator

class TestHappyPass:

    """
    Test Group that tests correct behavior of the calculator given valid data.
    Each test follows GIVEN-WHEN-THEN structure.
    """

    def test_addition(self):
        calculator = Calculator()
        a = 5
        b = 5
        expected = 10

        actual = calculator.add(a, b)

        assert actual == expected

    def test_addition_negative_value(self):
        calculator = Calculator()
        a = -5
        b = 5
        expected = 0

        actual = calculator.add(a, b)

        assert actual == expected

    def test_subtraction(self):
        calculator = Calculator()
        a = 10
        b = 7
        expected = 3

        actual = calculator.subtract(a, b)

        assert actual == expected

    def test_subtraction_negative_value(self):
        calculator = Calculator()
        a = -5
        b = 5
        expected = -10

        actual = calculator.subtract(a, b)

        assert actual == expected

    def test_multiplication(self):
        calculator = Calculator()
        a = 5
        b = 5
        expected = 25

        actual = calculator.multiply(a, b)

        assert actual == expected

    def test_multiplication_negative_value(self):
        calculator = Calculator()
        a = -5
        b = 5
        expected = -25

        actual = calculator.multiply(a, b)

        assert actual == expected


    def test_division(self):
        calculator = Calculator()
        a = 10
        b = 2
        expected = 5

        actual = calculator.divide(a, b)

        assert actual == expected

    def test_division_negative_value(self):
        calculator = Calculator()
        a = -5
        b = 5
        expected = -1

        actual = calculator.divide(a, b)

        assert actual == expected


class TestHappyFail:
    """
    Test Group that tests correct behavior of the calculator given invalid data.
    """

    def test_addition_invalid_value(self):
        calculator = Calculator()
        valid_param = 1
        invalid_param = "Invalid"

        with pytest.raises(TypeError):
            calculator.add(valid_param, invalid_param)

    def test_subtraction_invalid_value(self):
        calculator = Calculator()
        valid_param = 10
        invalid_param = "Invalid"

        with pytest.raises(TypeError):
            calculator.subtract(valid_param, invalid_param)

    def test_multiplication_invalid_value(self):
        calculator = Calculator()
        valid_param = 12
        invalid_param = None

        with pytest.raises(TypeError):
            calculator.multiply(valid_param, invalid_param)

    def test_division_invalid_value(self):
        calculator = Calculator()
        valid_param = 5
        invalid_param = "Invalid"

        with pytest.raises(TypeError):
            calculator.divide(valid_param, invalid_param)

    def test_zero_division(self):
        calculator = Calculator()
        valid_param = 5
        invalid_param = 0

        with pytest.raises(ZeroDivisionError):
            calculator.divide(valid_param, invalid_param)