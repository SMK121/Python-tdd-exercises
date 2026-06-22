

from calculate_discount import calculate_discount


# Test 1: standard 20% discount
def test_discount_20_percent():
    assert calculate_discount(100, 20) == 80


# Test 2: 50% discount
def test_discount_50_percent():
    assert calculate_discount(200, 50) == 100


# Test 3: no discount case
def test_no_discount():
    assert calculate_discount(50, 0) == 50


# Test 4: full discount (100%)
def test_full_discount():
    assert calculate_discount(80, 100) == 0