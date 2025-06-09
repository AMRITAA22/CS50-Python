from working import convert
import pytest
def test_full_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:30 PM to 2:45 AM") == "13:30 to 02:45"
def test_missing_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
def test_mixed_format():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("no time here")
