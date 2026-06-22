

from count_vowels import count_vowels


# Test 1: normal word
def test_hello():
    # hello contains e and o
    assert count_vowels("hello") == 2


# Test 2: all vowels
def test_all_vowels():
    # a e i o u = 5 vowels
    assert count_vowels("aeiou") == 5