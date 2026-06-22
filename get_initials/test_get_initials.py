

from get_initials import get_initials


# Test 1: Full name with two words
def test_two_names():
    # We expect "Neo Anderson" to return "NA"
    # N from Neo + A from Anderson
    assert get_initials("Neo Anderson") == "NA"


# Test 2: Single name only
def test_single_name():

    assert get_initials("Smith") == "S"