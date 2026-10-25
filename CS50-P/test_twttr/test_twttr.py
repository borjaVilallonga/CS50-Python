from twttr import shorten

def test_twttr():
    assert shorten("hi") == "h"
    assert shorten("La madre") == "L mdr"
    assert shorten("Paco") == "Pc"
    assert shorten("HELLO") == "HLL"
    assert shorten("1234") == "1234"
    assert shorten("Hello, word!") == "Hll, wrd!"

if __name__ == "__main__":
    main()
