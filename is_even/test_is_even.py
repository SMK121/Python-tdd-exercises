# Import the function to test
from is_even import is_even


# Test 1: check an even number
def test_even_number():

    assert is_even(4) == True


# Test 2: check an odd number
def test_odd_number():

    assert is_even(5) == False