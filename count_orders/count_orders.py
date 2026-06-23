

import sys  # used to access command-line arguments

# Get filename passed in terminal (e.g. orders.txt)
filename = sys.argv[1]

# Dictionary to store counts of each dish
counts = {}

# Open the file and process it line by line
with open(filename, "r") as file:
    for line in file:
        # Remove newline character and clean the dish name
        dish = line.strip()

        # Count each dish occurrence using dictionary
        counts[dish] = counts.get(dish, 0) + 1


# Print header for output
print("Order Summary")
print("-------------")


# Print each dish and how many times it appears
for dish, count in counts.items():
    print(f"{dish}: {count}")
