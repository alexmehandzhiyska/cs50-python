from bank import value

def test_starts_hello():
    assert(value('hello, its me')) == 0
    assert(value('Hello, its me')) == 0
    assert(value('HELLO, its me')) == 0

def test_starts_h():
    assert(value('hii, its me')) == 20
    assert(value('Hii, its me')) == 20
    assert(value('Helo, its me')) == 20

def test_starts_else():
    assert(value('asdf, its me')) == 100
    assert(value('ahdf, its me')) == 100