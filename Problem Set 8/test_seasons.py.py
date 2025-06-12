from seasons import minutes_to_words
from datetime import date
import pytest
from unittest.mock import patch

@patch("seasons.date")
def test_1999_01_01(mock_date):
    mock_date.today.return_value = date(2000, 1, 1)
    assert minutes_to_words(date(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"

@patch("seasons.date")
def test_2001_01_01(mock_date):
    mock_date.today.return_value = date(2003, 1, 1)
    assert minutes_to_words(date(2001, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"

@patch("seasons.date")
def test_1995_01_01(mock_date):
    mock_date.today.return_value = date(2000, 1, 1)
    assert minutes_to_words(date(1995, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"

@patch("seasons.date")
def test_2020_06_01(mock_date):
    mock_date.today.return_value = date(2032, 1, 1)
    assert minutes_to_words(date(2020, 6, 1)) == "Six million, ninety-two thousand, six hundred forty minutes"

@patch("seasons.date")
def test_1998_06_20(mock_date):
    mock_date.today.return_value = date(2000, 1, 1)
    assert minutes_to_words(date(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"
