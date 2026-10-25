from bank import value


def test_bank():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HeLlO") == 0

    assert value("H") == 20
    assert value("h") == 20
    assert value("Hi") == 20

    assert value("Good morning") == 100
    assert value("CAQUITA") == 100

