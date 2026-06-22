

def is_palindrome(text):
    """
    Check if a word reads the same forwards and backwards.
    """

    # reverse the text using slicing
    reversed_text = text[::-1]

    # compare original with reversed
    return text == reversed_text


print(is_palindrome("madam"))   # True
print(is_palindrome("hello"))   # False