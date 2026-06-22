

def count_words(sentence):
    # Split sentence into individual words
    words = sentence.split()

    # Create empty dictionary to store word counts
    word_count = {}

    # Loop through each word
    for word in words:

        # If word already exists in dictionary
        if word in word_count:
            # Increase its count by 1
            word_count[word] += 1
        else:
            # Otherwise add it with count 1
            word_count[word] = 1

    # Return final dictionary
    return word_count

# manual test
print(count_words("apple banana apple"))