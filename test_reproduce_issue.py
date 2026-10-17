from unittest.mock import patch
import pytest

# Safely import simpleCalc in case top-level script execution calls input()
with patch("builtins.input", side_effect=["0", "0", "+"]):
    import simpleCalc


def test_reproduce_zero_division():
    """Test that division by zero returns an error message rather than raising ZeroDivisionError."""
    result = simpleCalc.operation(10, 0, "/")
    assert result == "Error: Division by zero"


def test_addition():
    assert simpleCalc.operation(5, 3, "+") == 8


def test_subtraction():
    assert simpleCalc.operation(10, 4, "-") == 6


def test_multiplication():
    assert simpleCalc.operation(4, 5, "*") == 20


def test_valid_division():
    assert simpleCalc.operation(10, 2, "/") == 5.0