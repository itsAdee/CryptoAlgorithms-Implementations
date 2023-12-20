import frequqncyanalysis


def index_of_coincidence(freq):
    """Calculates the index of coincidence for a given ciphertext"""
    

    # Calculate the index of coincidence
    N = sum(freq.values())
    ic = sum([freq[letter] * (freq[letter] - 1) for letter in freq]) / (N * (N - 1))

    return ic

# Read the ciphertext from a file
with open("Ctext-2.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')

# Perform a frequency analysis on the ciphertext
freq = frequqncyanalysis.frequency_analysis(ciphertext)

# Calculate the index of coincidence
ic = index_of_coincidence(freq)

# Print the index of coincidence
print(ic)

