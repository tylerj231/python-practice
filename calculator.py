class Calculator:
    """
    Object representing a simple calculator with basic operations.
    """

    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a, b) -> int:
        return a - b

    def multiply(self, a: int, b) -> int:
        return a * b

    def divide(self, a: int, b) -> int:
        return a / b

    def __repr__(self):
        return "Calculator()"
