

from mask_email import mask_email  # import function to test


# Test 1: basic email masking
def test_basic_email():
    # Check simple email is masked correctly
    assert mask_email("neo@gmail.com") == "n**@gmail.com"


# Test 2: longer username email
def test_long_email():
    # Check longer username is fully masked except first letter
    assert mask_email("neo.anderson@yahoo.com") == "n***********@yahoo.com"