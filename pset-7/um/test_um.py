from um import count

def test_count_multiple_um():
    assert(count('thanks um for the album')) == 1
    assert(count('test, um, test, um')) == 2

def test_count_0_um():
    assert(count('test, test, m')) == 0

def test_starts_with_um():
    assert(count('Um, test')) == 1
    assert(count('Um, test, um')) == 2

def test_um_is_substring():
    assert(count('test yummy')) == 0
    assert(count('Um, test yummy, um')) == 2
    assert(count('Um, test yummy, umm, um')) == 2