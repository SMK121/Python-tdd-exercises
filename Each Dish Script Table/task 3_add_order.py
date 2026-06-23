

import sys
import json

# Get table + dish from terminal
table = sys.argv[1]
dish = " ".join(sys.argv[2:])

filename = "each_order.json"

# Load existing data or start empty
try:
    with open(filename, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}

# If table doesn't exist yet, create it
if table not in data:
    data[table] = []

# Add dish to that table
data[table].append(dish)

# Save back to file
with open(filename, "w") as file:
    json.dump(data, file, indent=4)

print("Order added:", table, dish)