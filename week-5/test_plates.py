from plates import is_valid
import pytest

def test_start_two_letters():
    assert is_valid("AAJ285") == True
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_max_6_char():
    assert is_valid("AA2222222") == False
    assert is_valid("HAAH984") == False
    
def test_num_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("GB45A") == False
    
def test_special_chars():
    assert is_valid("HaHa123!") == False
    assert is_valid("$MOOLA1") == False

def test_no_input():
    with pytest.raises(TypeError):
        is_valid()