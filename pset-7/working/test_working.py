import pytest
from working import convert

def test_convert_only_hours():
    assert(convert('9 AM to 5 PM')) == '09:00 to 17:00'
    assert(convert('8 PM to 3 AM')) == '20:00 to 03:00'

def test_convert_hour_12():
    assert(convert('12:00 PM to 5:25 AM')) == '12:00 to 05:25'
    assert(convert('12:00 AM to 5:25 AM')) == '00:00 to 05:25'
    
def test_convert_hours_mins():
    assert(convert('9:00 AM to 5:00 PM')) == '09:00 to 17:00'
    assert(convert('9:30 PM to 5:25 AM')) == '21:30 to 05:25'

def test_convert_invalid_mins():
    with pytest.raises(ValueError):
        convert('9:60 AM to 10:30 PM')

    with pytest.raises(ValueError):
        convert('9:30 AM to 10:60 PM')

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert('9:30 AM - 10:30 PM')