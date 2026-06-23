

import sys  # access command-line arguments from the terminal

# Get all values passed after the script name (supports multi-word dishes)
dish = " ".join(sys.argv[1:])

# Open the file in append mode (adds new orders without deleting old ones)
with open("order.txt", "a") as file:
    file.write(dish + "\n")

# Confirm to the user that the order was saved successfully
print("Order added:", dish)