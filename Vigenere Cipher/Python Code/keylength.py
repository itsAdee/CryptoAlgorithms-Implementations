import frequqncyanalysis,indexofconfidence

def estimate_key_length(ciphertext):
    """Estimates the key length of a Vigenere ciphertext using the index of coincidence"""
    # Calculate the index of coincidence for the ciphertext
    freq = frequqncyanalysis.frequency_analysis(ciphertext)
    ic = indexofconfidence.index_of_coincidence(freq)
    print("Index of coincidence:", ic)

    # Estimate the key length
    N = len(ciphertext)
    key_length = 0
    max_ic = 0
    for i in range(1, N):
        subtext1 = ciphertext[:i]
        subtext2 = ciphertext[i:2*i]
        comb=subtext1+subtext2
        freq = frequqncyanalysis.frequency_analysis(comb)
        ic = indexofconfidence.index_of_coincidence(freq)
        if ic > max_ic:
            max_ic = ic
            key_length = i

    return key_length

# Read the ciphertext from a file
with open("Ctext-2.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')

# Estimate the key length
key_length = estimate_key_length(ciphertext)
print("Estimated key length:", key_length)
