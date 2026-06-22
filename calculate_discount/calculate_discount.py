

def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying a percentage discount.

    Args:
        price (float or int): original price of item
        discount_percent (float or int): discount percentage (e.g. 20 for 20%)

    Returns:
        float: final price after discount
    """

    # Convert percentage into a decimal value and calculate discount amount
    discount_amount = price * (discount_percent / 100)

    # Subtract discount from original price
    final_price = price - discount_amount

    # Return final result
    return final_price


print("Test 1: 100 with 20% discount")
print(calculate_discount(100, 20))  # expected: 80

print("Test 2: 200 with 50% discount")
print(calculate_discount(200, 50))  # expected: 100

