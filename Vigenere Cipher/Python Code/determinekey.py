import frequqncyanalysis,indexofconfidence,keylength

def determine_key(ciphertext, key_length):
    """Determines the key of a Vigenere ciphertext using frequency analysis"""
    # Divide the ciphertext into subtexts with a length equal to the key length
    subtexts = [ciphertext[i::key_length] for i in range(key_length)]

    # Perform frequency analysis on each subtext
    subtext_freqs = [frequqncyanalysis.frequency_analysis(subtext) for subtext in subtexts]

    # Determine the key
    key = ""
    for i in range(key_length):
        max_freq = max(subtext_freqs[i], key=subtext_freqs[i].get)
        shift = ord(max_freq) - ord("E")
        key += chr((shift + 26) % 26 + ord("A"))

    return key

# Read the ciphertext from a file
with open("Ctext-2.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')

# Estimate the key length
key_length = keylength.estimate_key_length(ciphertext)

# Determine the key
key = determine_key(ciphertext, 5)
print("Key:", key)
