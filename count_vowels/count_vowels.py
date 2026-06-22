

def count_vowels(text):

    vowels = "aeiou"

    count = 0

    # Loop through each character in the text
    for letter in text:

        # Check if letter is a vowel
        if letter.lower() in vowels:

            # Add 1 to count
            count += 1

    # Return total number of vowels
    return count

# manual test
print(count_vowels("hello"))