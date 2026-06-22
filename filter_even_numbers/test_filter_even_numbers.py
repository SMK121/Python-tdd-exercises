

from filter_even_numbers import filter_even_numbers


# Test 1: mixture of odd and even numbers
def test_mixed_numbers():
    # Only even numbers should be returned
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


# Test 2: all numbers are even
def test_all_even():
    # Entire list should be returned
    assert filter_even_numbers([2, 4, 6]) == [2, 4, 6]