from um import count
import pytest

def test_alone():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um um") == 2
    
def test_sentence():
    assert count("hello, um, world") == 1
    assert count("This is um my life um aware um") == 3
    
def test_long_um():
    assert count("umm") == 0
    assert count(" ummmmmm ") == 0
    assert count("hello, ummm, world") == 0
    
def test_word():
    assert count("theorum") == 0
    assert count(" yummy ") == 0
    assert count("theo um") == 1