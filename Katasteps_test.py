import Katasteps
from Katasteps import NegativesNotAllowed
import pytest


def test_on_empty_string():
    assert Katasteps.add("") == 0

def test_on_single_digit():
    assert Katasteps.add("5") == 5

def test_on_two_digits():
    assert Katasteps.add("2,3") == 5

def test_on_number_of_digits():
    assert Katasteps.add("1,2,3,4,5") == 15

def test_newlines():
    assert Katasteps.add("1,\n2")

def test_on_numbers_bigger_than_1000():
    assert Katasteps.add("1001,2") == 2

def testing_negatives():
    with pytest.raises(NegativesNotAllowed) as excinfo:
        Katasteps.add("-2,-3")
    assert "Negatives not allowed" in str(excinfo.value)
