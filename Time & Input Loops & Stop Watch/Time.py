

import time

print(time.time())
print(time.ctime())


# Function that calculates how long multiplication takes
def multiple_time(num1, num2):

    time1 = time.perf_counter()

    product = num1 * num2

    time2 = time.perf_counter()

    print(f"The answer is {product} - this took {time2 - time1} seconds.")


# multiple_time(5, 10)
#
# print("Pausing for 5 seconds....")
# time.sleep(5)
# print("Pause Completed")


name = input("What's your name? ")
print(f"Hello, {name}!")


ask_again = True
while ask_again:

    proceed = input("Would you like to proceed? (Y/N\v>").upper()
    if proceed == "Y":
      print("Proceeding...!")
    elif proceed == "N":
     print("Stopping!")
     ask_again = False
