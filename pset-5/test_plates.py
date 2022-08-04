from plates import is_valid

def test_starts_2_letters():
    assert(is_valid('CS50')) == True
    assert(is_valid('C50')) == False
    assert(is_valid('CSS50')) == True

def test_has_max_6_chars():
    assert(is_valid('C')) == False
    assert(is_valid('CS500000')) == False
    assert(is_valid('CS5000')) == True

def test_has_middle_numbers():
    assert(is_valid('CS50P')) == False
    assert(is_valid('CSP')) == True

def test_first_digit_0():
    assert(is_valid('CS05')) == False
    assert(is_valid('CS15')) == True

def test_has_special_chars():
    assert(is_valid('CS.50')) == False
    assert(is_valid('CS,50')) == False
    assert(is_valid('CS_50')) == False
    assert(is_valid('CS?50')) == False
    assert(is_valid('CS!50')) == False