from numb3rs import validate

def test_input_string():
    assert(validate('cat')) == False
    assert(validate('cat.dog.duck.manioka')) == False

def test_ip_too_short():
    assert(validate('122.1.4')) == False

def test_ip_too_long():
    assert(validate('122.1.4.56.20')) == False

def test_num_less_than_0():
    assert(validate('-4.133.133.133')) == False
    assert(validate('4.-133.133.133')) == False
    assert(validate('4.133.-133.133')) == False
    assert(validate('4.133.133.-133')) == False

def test_num_0():
    assert(validate('0.0.0.0')) == True
    assert(validate('0.122.56.32')) == True
    assert(validate('122.0.56.32')) == True
    assert(validate('122.32.0.32')) == True
    assert(validate('122.32.51.0')) == True

def test_num_greater_than_255():
    assert(validate('256.23.120.120')) == False
    assert(validate('0.256.120.120')) == False
    assert(validate('0.4.256.120')) == False
    assert(validate('0.4.23.256')) == False

def test_num_255():
    assert(validate('255.132.12.1')) == True
    assert(validate('22.255.12.1')) == True
    assert(validate('22.45.255.1')) == True
    assert(validate('22.45.120.255')) == True
    assert(validate('255.255.255.255')) == True