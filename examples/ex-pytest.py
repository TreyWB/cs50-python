from response import validate_email
import pytest

def test_valid():
    assert validate_email("email@example.com") == "Valid"
    assert validate_email("firstname.lastname@example.com") == "Valid"
    assert validate_email("email@123.123.123.123") == "Valid"

def test_invalid():
    assert validate_email("#@%^%#$@#$@#.com") == "Invalid"
    assert validate_email("”(),:;<>[\]@example.com") == "Invalid"
    assert validate_email("@example.com") == "Invalid"
    assert validate_email("email..email@example.com") == "Invalid"
    
def test_spaces():
    assert validate_email("My email is test@test.com") == "Invalid"
    assert validate_email("email @email.com") == "Invalid"
    
def test_no_tld():
    assert validate_email("email@example") == "Invalid"

def test_int():
    with pytest.raises(TypeError):
        validate_email(1)
    
def test_none():
    assert validate_email("") == "Invalid"
    
    with pytest.raises(SystemError, match="You must provide an email address"):
        validate_email()