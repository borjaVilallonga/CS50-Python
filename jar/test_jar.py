from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("12")
    with pytest.raises(ValueError):
        Jar(12.5)

def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar= Jar()

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(4)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.deposit(10)

    assert jar.size == 7

def test_withdraw():
    jar = Jar()

    jar.deposit(10)

    jar.withdraw(3)
    assert jar.size == 7

    jar.withdraw(2)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.withdraw(6)

    assert jar.size == 5
