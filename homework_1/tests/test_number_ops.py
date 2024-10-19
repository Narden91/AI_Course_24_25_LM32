import pytest
from src.homework.number_ops import fibonacci_recursive, sum_of_digits_recursive, is_palindrome_number


def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(8) == 21


def test_fibonacci_recursive_negative():
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)


def test_sum_of_digits_recursive():
    assert sum_of_digits_recursive(12345) == 15
    assert sum_of_digits_recursive(0) == 0
    assert sum_of_digits_recursive(-123) == 6


def test_is_palindrome_number():
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(12345) == False
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(-12321) == False
