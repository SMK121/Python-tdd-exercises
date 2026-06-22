

import sys  # used to read command-line arguments

# STEP 1: Check user provided a dish name
if len(sys.argv) != 2:
    print("Usage: python add_order.py <dish_name>")
    sys.exit()

# STEP 2: Get dish name from command line
dish = sys.argv[1]

# STEP 3: Append dish to file
with open("orders.txt", "a") as file:
    file.write(dish + "\n")

# STEP 4: Confirmation message
print("Order added:", dish)