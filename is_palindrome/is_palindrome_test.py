

from is_palindrome import is_palindrome

def test_palindrome_true():

    # madam reads the same backwards

    assert is_palindrome("madam") == True

def test_palindrome_false():

    # hello does NOT read the same backwards

    assert is_palindrome("hello") == False

