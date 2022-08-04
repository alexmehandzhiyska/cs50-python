from multiprocessing.sharedctypes import Value
from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert(convert('3/4')) == 75
    assert(convert('1/4')) == 25
    assert(convert('4/4')) == 100

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert('5/4')

def test_convert_not_int():
    with pytest.raises(ValueError):
        convert('4.5/5')

    with pytest.raises(ValueError):
        convert('4/5.2')

def test_convert_y_0():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_gauge_valid():
    assert(gauge(2)) == '2%'
    assert(gauge(35)) == '35%'
    assert(gauge(75)) == '75%'
    assert(gauge(98)) == '98%'

def test_gauge_full():
    assert(gauge(100)) == 'F'
    assert(gauge(99)) == 'F'

def test_gauge_empty():
    assert(gauge(0)) == 'E'
    assert(gauge(1)) == 'E'