import pytest

from badges import add, divide, subtract


def test_add() -> None:
    assert add(1.5, 2.5) == 4.0


def test_subtract() -> None:
    assert subtract(10, 3) == 7


def test_divide() -> None:
    assert divide(9, 3) == 3


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Division by zero"):
        divide(1, 0)
