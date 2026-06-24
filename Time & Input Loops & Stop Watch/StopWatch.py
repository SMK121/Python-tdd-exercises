

# 1 Build Python Stopwatch Enter to start, Enter to stop, how long has elapsed

# 2 As a bonus, can you add a lap timer? # Or a log of previous times?


import time

history = []  # store past times


def stopwatch():
    print("=== Stopwatch ===")
    print("ENTER = start / stop, CTRL+C = quit\n")

    while True:
        try:
            input("Press ENTER to start...")    # wait to start
            start = time.perf_counter()         # start timer

            input()  # wait to stop
            end = time.perf_counter()           # stop timer

            total = end - start                 # calculate time

            print(f"Time: {total:.2f} seconds") # displays result clearly

            history.append(total)               # save result in history 

            cont = input("ENTER to run again or 'q' to quit: ")  # user decision
            if cont.lower() == "q":
                break

        except KeyboardInterrupt:
            print("\nStopped.")
            break

    print("History:", [round(t, 2) for t in history])  # show all times


stopwatch()





