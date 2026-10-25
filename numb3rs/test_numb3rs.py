from numb3rs import validate

def test_validate():
    # Valid IPv4 addresses
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
    assert validate("45.76.255.1") == True
    assert validate("255.255.3.255") == True

    # Invalid values in each byte
    assert validate("500.255.255.255") == False
    assert validate("255.500.255.255") == False
    assert validate("255.255.500.255") == False
    assert validate("255.255.255.500") == False
    assert validate("256.255.255.255") == False

    # Invalid format
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False

    # Leading zeros
    assert validate("000.001.010.100") == False



