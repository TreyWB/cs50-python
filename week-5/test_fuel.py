from fuel import convert, gauge
import pytest

def test_percentage():
    assert convert("2 / 3") == 67
    assert convert("15 / 17") == 88
    
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(70) == "70%"

def test_no_input():
    with pytest.raises(TypeError):
        convert()
        
    with pytest.raises(TypeError):
        gauge()