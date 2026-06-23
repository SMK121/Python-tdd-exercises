

import json  # used to work with JSON files (read/write structured data)

# Name of the JSON file that stores all orders
filename = "each_order.json"

# Open the JSON file and load its contents into a Python dictionary
with open(filename, "r") as file:
    data = json.load(file)

# Print heading for output
print("Order Summary by Table")
print("----------------------")

# Loop through each table in the data
for table, orders in data.items():
    print(table)  # print table name (e.g. Table 12)

    # Loop through all dishes for that table
    for dish in orders:
        print(" -", dish)  # print each dish under the table