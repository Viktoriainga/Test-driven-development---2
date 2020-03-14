import Katasteps

def test_on_empty_string():
    assert Katasteps.add("") == 0

def test_on_single_digit():
    assert Katasteps.add("5") == 5

def test_on_two_digits():
    assert Katasteps.add("2,3") == 5

def test_on_number_of_digits():
    assert Katasteps.add("1,2,3,4,5") == 15
