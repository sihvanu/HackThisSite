def unscramble_words(scrambled_words):
    # Load a wordlist or dictionary
    with open("wordlist.txt", "r") as file:
        wordlist = [word.strip() for word in file.readlines()]

    # Unscramble the words
    unscrambled_words = []
    for scrambled_word in scrambled_words:
        for word in wordlist:
            if sorted(scrambled_word) == sorted(word):
                unscrambled_words.append(word)
                break

    return unscrambled_words


# Prompt the user for scrambled words
scrambled_words = []
print("Enter the scrambled words (one word per line). Enter an empty line to finish:")
while True:
    word = input()
    if not word:
        break
    scrambled_words.append(word)

# Unscramble the words
unscrambled = unscramble_words(scrambled_words)

# Print the unscrambled words as a comma-separated list
print(", ".join(unscrambled))
