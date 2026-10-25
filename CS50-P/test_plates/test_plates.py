from plates import is_valid

def test_beginning_alphabetical():
    assert not is_valid("1A")
    assert not is_valid("A1")

def test_length():
    assert not is_valid("A")
    assert not is_valid("ABCDEFG")


def test_number_placement():
    assert not is_valid("AB12C")
    assert not is_valid("AB1C2")


def test_zero_placement():
    assert not is_valid("AB0123")
    assert not is_valid("AB0094")


def test_alphanumeric():
    assert not is_valid("AB12!")
    assert not is_valid("AB-12")
    assert not is_valid("AB 12")


def test_valid():
    assert is_valid("AB")
    assert is_valid("AB1234")
    assert is_valid("ABC123")
