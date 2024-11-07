from bank import value
import pytest

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlO") == 0

def test_letter_h():
    assert value("hi") == 20
    assert value("heyo!") == 20
    assert value("HIYA") == 20

def test_non_h():
    assert value("yo") == 100
    assert value("YOGE") == 100
    assert value("Wagwan?") == 100

def test_no_greeting():
    with pytest.raises(TypeError):
        value()
