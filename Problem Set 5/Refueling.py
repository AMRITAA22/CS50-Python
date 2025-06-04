import pytest
from fuel import convert, gauge
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/1") == 0
def test_convert_invalid_value():
    with pytest.raises(ValueError):
        convert("3/a")
    with pytest.raises(ValueError):
        convert("5/3")  # x > y
    with pytest.raises(ValueError):
        convert("cat/dog")
def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge_extremes():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
