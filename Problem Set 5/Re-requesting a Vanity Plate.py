from plates import is_valid
def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("XYZ123") == True
def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
def test_invalid_start():
    assert is_valid("1CS50") == False
    assert is_valid("C5") == False
def test_numbers_in_middle_or_start_with_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS5O5") == False
    assert is_valid("CS50X") == False
def test_non_alphanumeric():
    assert is_valid("CS 50") == False
    assert is_valid("CS!50") == False
