from NUMB3RS import validate
import pytest

def test_validate():
    assert validate("1.2.3.4") == "True"
    assert validate("255.255.255.255") == "True"
    assert validate("8.8.8.8") == "True"

    assert validate("-1.-1.-1.-1") == "False"
    assert validate("275.0.1.800") == "False"