

from find_longest_word import find_longest_word


def test_basic_case():
    # "elephant" is the longest word (8 letters)
    assert find_longest_word(["cat", "elephant", "dog"]) == "elephant"


def test_tie_case():
    # all words same length → first one is returned
    assert find_longest_word(["car", "bus", "van"]) == "car"