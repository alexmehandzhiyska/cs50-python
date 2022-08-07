from seasons import validate_date


def test_validate_date_valid_dates():
    assert(validate_date('2004-10-07')) == True
    assert(validate_date('1992-02-12')) == True

def test_validate_date_wrong_format():
    assert(validate_date('2004.10.07')) == False
    assert(validate_date('2004/10/07')) == False

def test_validate_date_invalid_year():
    assert(validate_date('20-10-07')) == False
    assert(validate_date('22345-10-07')) == False

def test_validate_date_invalid_month():
    assert(validate_date('2004-1-07')) == False
    assert(validate_date('2007-123-07')) == False

def test_validate_date_invalid_day():
    assert(validate_date('2004-10-7')) == False
    assert(validate_date('1934-05-721')) == False

