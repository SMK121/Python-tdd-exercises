

def most_common_item(items):
    counts = {}

    # Count how many times each item appears
    for item in items:

        # If item already exists, increase count
        if item in counts:
            counts[item] += 1
        else:
            # First time seeing item
            counts[item] = 1

    # Start by assuming first item is most common
    most_common = items[0]

    # Loop through dictionary
    for item in counts:

        # If current item count is bigger
        if counts[item] > counts[most_common]:
            most_common = item

    # Return most common item
    return most_common

# Manual test
print(most_common_item(["apple", "banana", "apple", "orange", "apple"]))