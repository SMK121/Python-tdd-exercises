

from count_words import count_words


def test_basic_sentence():
    assert count_words("apple banana apple") == {
        "apple": 2,
        "banana": 1
    }


def test_single_word():
    assert count_words("test test test") == {
        "test": 3
    }