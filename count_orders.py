

import sys  # used to read filename from terminal

# -------------------------------
# STEP 1: Check correct usage
# -------------------------------
# Example run:
# python count_orders.py order.txt
if len(sys.argv) != 2:
    print("Usage: python count_orders.py <filename>")
    sys.exit()

# Get filename from command-line input
filename = sys.argv[1]

# -------------------------------
# STEP 2: Read the file
# -------------------------------
# "r" = read mode (we are NOT changing the file)
with open(filename, "r") as file:
    lines = file.readlines()  # reads all lines into a list

# -------------------------------
# STEP 3: Create dictionary for counting
# -------------------------------
# Dictionary stores:
# dish → number of times it appears
# Example:
# {"Curry": 2, "Rice": 1}
counts = {}

# -------------------------------
# STEP 4: Loop through each line
# -------------------------------
for line in lines:
    dish = line.strip()  # removes \n (new line character)

    # If dish already exists in dictionary → increase count
    if dish in counts:
        counts[dish] += 1
    else:
        counts[dish] = 1

# -------------------------------
# STEP 5: Print results
# -------------------------------
print("\nOrder Summary")
print("-------------")

for dish, count in counts.items():
    print(dish + ":", count)