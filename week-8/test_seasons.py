from seasons import main
import pytest

def test_years():
    assert main("2020-12-05") == "One million, six hundred forty-one thousand, six hundred minutes"

    assert main("1994-01-01") == "Fifteen million, eight hundred four thousand minutes"

    assert main("1995-02-06") == "Fifteen million, two hundred twenty-six thousand, five hundred sixty minutes"

    assert main("2024-01-18") == "One thousand, four hundred forty minutes"

    assert main("2023-01-19") == "Five hundred twenty-five thousand, six hundred minutes"