from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()

    jar.deposit(3)
    assert jar.__str__() == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    
    assert jar.size == 0
    
    jar.deposit(7)
    assert jar.size == 7

    jar.deposit(2)
    assert jar.size == 9

def test_withdraw():
    jar = Jar()
    
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7

    jar.withdraw(1)
    assert jar.size == 6

    jar.withdraw(1)
    jar.deposit(1)
    assert jar.size == 6

def test_withdraw_fail():
    jar = Jar()
    
    jar.deposit(1)

    with pytest.raises(SystemExit, match="\nNot enough cookies in jar to remove"):
        jar.withdraw(10)

def test_deposit_error():
    jar = Jar()
    
    with pytest.raises(SystemExit, match="\nJar capacity exceeded"):
        jar.deposit(99)

def test_capacity_error():
    with pytest.raises(SystemExit, match="\nCapacity must be a positive number"):
        jar = Jar(capacity=-5)