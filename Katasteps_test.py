import Katasteps

def test_on_empty_string():
    assert Katasteps.add("") == 0

def test_on_single_digit():
    assert Katasteps.add("5") == 5

def test_on_two_digits():
    assert Katasteps.add("2,3") == 5