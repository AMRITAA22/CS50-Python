from numb3rs import validate
def test_valid_addresses():
    assert validate("192.168.1.1") is True
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("1.2.3.4") is True
def test_invalid_numbers():
    assert validate("256.0.0.1") is False
    assert validate("275.3.6.28") is False
    assert validate("-1.2.3.4") is False
    assert validate("123.456.78.90") is False
    assert validate("192.168.1.300") is False
def test_invalid_formats():
    assert validate("192.168.1") is False
    assert validate("192.168.1.1.1") is False
    assert validate("192,168,1,1") is False
    assert validate("abc.def.ghi.jkl") is False
    assert validate("") is False
    assert validate("...") is False
