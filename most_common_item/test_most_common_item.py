

from most_common_item import most_common_item


# Test 1: normal case
def test_common_fruit():
    assert most_common_item(
        ["apple", "banana", "apple", "orange", "apple"]
    ) == "apple"


# Test 2: numbers work too
def test_common_number():
    assert most_common_item(
        [1, 2, 2, 3, 2]
    ) == 2