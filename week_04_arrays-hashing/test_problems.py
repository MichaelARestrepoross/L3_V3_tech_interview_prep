from problems import contains_duplicate, two_sum, is_anagram

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1])
    assert not contains_duplicate([1,2,3])
    # Additional unique test case: large list with a single duplicate
    assert contains_duplicate([10, 20, 30, 40, 50, 10])

def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]
    # test case: multiple valid pairs, matches function behavior
    assert two_sum([1, 3, 2, 4], 5) == [1, 2]

def test_is_anagram():
    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")
    # test case: case-insensitive anagram
    assert is_anagram("Listen", "Silent")