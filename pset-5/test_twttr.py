from twttr import shorten

def test_no_vowels():
    assert shorten('tst') == 'tst'
    assert shorten('sdf') == 'sdf'

def test_vowels():
    assert shorten('atest') == 'tst'
    assert shorten('hello, its me') == 'hll, ts m'

def test_uppercase():
    assert shorten('ATEST1') == 'TST1'
    assert shorten('hEllo, Its me') == 'hll, ts m'