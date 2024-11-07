from working import parse
import pytest

def test_parse():
    assert parse("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert parse("10:00 AM to 11:00 PM") == "10:00 to 23:00"
    
    assert parse("9 AM to 5 PM") == "09:00 to 17:00"
    assert parse("12 AM to 10 PM") == "00:00 to 22:00"
    
    assert parse("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert parse("10:45 AM to 12 PM") == "10:45 to 12:00"

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        parse("cat")
    assert pytest_wrapped_e.type == SystemExit
    assert str(pytest_wrapped_e.value) == "Improper Formatting"

    with pytest.raises(TypeError):
        parse()