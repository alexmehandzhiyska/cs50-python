from jar import Jar
import pytest

def test_str_empty():
    jar = Jar()
    assert str(jar) == ''

def test_str_2():
    jar = Jar(4)
    jar.deposit(2)

    assert str(jar) == '🍪🍪'

def test_deposit():
    jar = Jar(5)

    jar.deposit(2)
    assert jar.size == 2

    jar.deposit(1)
    assert jar.size == 3

def test_deposit_capacity_exceeded():
    jar = Jar(1)

    with pytest.raises(ValueError):
        assert jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(1)

    assert jar.size == 3

def test_withdraw_insufficient_size():
    jar = Jar(5)
    jar.deposit(2)
    
    with pytest.raises(ValueError):
        assert jar.withdraw(3)