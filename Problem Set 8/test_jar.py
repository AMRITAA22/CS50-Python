import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("a")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(4)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(2)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.deposit(1)  # would exceed capacity

def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)  # not enough cookies
