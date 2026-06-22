

def find_longest_word(words):
    
    longest = words[0]

    # Loop through each word in the list
    for word in words:

        # If current word is longer than the current longest
        if len(word) > len(longest):
            # Replace longest with this word
            longest = word

    # Return the longest word found
    return longest

print(find_longest_word(["cat", "elephant", "dog"]))