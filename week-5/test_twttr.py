from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello, how are you?") != "hll, hw re y?"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Hello, How Are You?") != "Hll, How r Y?"


def test_digits_symbols():
    assert shorten("CS50") == "CS50"
    assert shorten("Hello!") != "Hell!"


def test_begin_with_vowel():
    assert shorten("I'm Coping Really Hard") == "'m Cpng Rlly Hrd"
    assert shorten("Alexa, play Despacito") != "lx, ply Dspcto"


def test_no_input():
    with pytest.raises(TypeError):
        shorten()