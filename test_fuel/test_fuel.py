import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("3/3") == 100

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
            convert("dog")

    with pytest.raises(ValueError):
            convert("-1/3")

    with pytest.raises(ValueError):
            convert("4/3")

def test_gauge():
     assert gauge(100) == "F"
     assert gauge(99) == "F"
     assert gauge(1) == "E"
     assert gauge(98) == "98%"




