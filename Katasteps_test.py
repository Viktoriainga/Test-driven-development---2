import Katasteps

def test_on_empty_string():
    assert Katasteps.add("") == 0

def test_on_single_digit():
    assert Katasteps.add("5") == 5