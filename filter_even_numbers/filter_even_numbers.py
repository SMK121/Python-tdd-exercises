

def filter_even_numbers(numbers):
    # Create empty list to store even numbers
    even_numbers = []

    # Loop through each number in the list
    for number in numbers:

        # Check if number is even
        if number % 2 == 0:

            # Add even number to the new list
            even_numbers.append(number)

    # Return list of even numbers
    return even_numbers

# Manual test
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))