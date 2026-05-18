## Requirements

Write a `Calculator` class with `add`, `subtract`, `multiply`, `divide`. Then write `test_calculator.py` with at least 10 tests covering:

- Happy path for all 4 operations
- `divide(10, 0)` → raises `ZeroDivisionError`
- Negative numbers, floats, large numbers

## 🗂 Test Data

```python
calc = Calculator()

# These must all pass:
calc.add(2, 3)          # → 5
calc.add(-1, 1)         # → 0
calc.subtract(10, 4)    # → 6
calc.subtract(0, 5)     # → -5
calc.multiply(3, 4)     # → 12
calc.multiply(-2, -3)   # → 6
calc.multiply(0, 999)   # → 0
calc.divide(10, 2)      # → 5.0
calc.divide(7, 2)       # → 3.5
calc.divide(10, 0)      # → ZeroDivisionError
```

## ✅ Expected Output

```
$ pytest test_calculator.py -v

test_calculator.py::test_add_positive          PASSED
test_calculator.py::test_add_negative          PASSED
test_calculator.py::test_add_zero              PASSED
test_calculator.py::test_subtract_basic        PASSED
test_calculator.py::test_subtract_negative     PASSED
test_calculator.py::test_multiply_basic        PASSED
test_calculator.py::test_multiply_negative     PASSED
test_calculator.py::test_multiply_zero         PASSED
test_calculator.py::test_divide_basic          PASSED
test_calculator.py::test_divide_float          PASSED
test_calculator.py::test_divide_by_zero        PASSED

========== 11 passed in 0.04s ==========
```

## 🐙 Submission

Push both `calculator.py` and `test_calculator.py` to: `python-practice/testing/`