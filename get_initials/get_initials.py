

def get_initials(name):
    # Split the name into separate words
    parts = name.split()

    # String to store initials
    initials = ""

    # Loop through each word in the name
    for part in parts:

        # Add the first letter of the word to initials
        initials += part[0]

    # Return the completed initials
    return initials


# manual test
print(get_initials("Neo Anderson"))
