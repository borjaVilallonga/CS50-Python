from um import count

def test_count():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("Um, thanks, um, regular expressions") == 2
    assert count("Um Um uM um") == 4
    assert count("Mum, yummy, album, plumber, drums") == 0
    assert count("um") == 1
    assert count("um... um! um?") == 3

