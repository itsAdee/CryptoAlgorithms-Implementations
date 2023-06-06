def frequency_analysis(ciphertext):
    """Performs a frequency analysis on a given ciphertext"""
    # Create a dictionary to store the frequency of each letter
    freq = {}
    for i in range(26):
        freq[chr(i + ord('A'))] = 0

    # Count the frequency of each letter in the ciphertext
    for letter in ciphertext:
        if letter.isalpha():
            freq[letter.upper()] += 1

    # Sort the letters by frequency
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

    return freq

# Read the ciphertext from a file
with open("Ctext-1.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')

# Perform a frequency analysis on the ciphertext
freq = frequency_analysis(ciphertext)

# Print the frequency of each letter
for letter, count in freq.items():
    print(letter + ": " + str(count))
