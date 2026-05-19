import pytest

from tasks.calculator import Calculator


@pytest.fixture(scope="session")
def calculator():
    """
    Provide a valid calculator instance for whole test session.
    :return: Calculator instance
    """
    calculator = Calculator()
    yield calculator
