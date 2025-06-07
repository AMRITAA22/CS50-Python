from twttr import shorten
def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""
def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
def test_mixed_case():
    assert shorten("Twitter") == "Twttr"
def test_numbers():
    assert shorten("t3st1ng") == "t3st1ng"
def test_symbols():
    assert shorten("hello!") == "hll!"
def test_empty():
    assert shorten("") == ""
def test_sentence():
    assert shorten("Hello, World!") == "Hll, Wrld!"
