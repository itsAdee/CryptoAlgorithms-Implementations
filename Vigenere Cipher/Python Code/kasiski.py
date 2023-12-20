
def kasiski_examination(ciphertext):
    """Determines the key length of a Vigenere ciphertext using Kasiski examination"""
    # Find all repeated sequences of at least three letters in the ciphertext
    repeats = {}
    for i in range(len(ciphertext) - 2):
        seq = ciphertext[i:i+3]
        if seq in repeats:
            repeats[seq].append(i)
        else:
            repeats[seq] = [i]

    # Calculate the distance between each pair of repeated sequences
    distances = []
    for seq, indices in repeats.items():
        if len(indices) > 1:
            for i in range(1, len(indices)):
                distances.append(indices[i] - indices[i-1])

    # Find the most common factors among the distances
    factors = {}
    for distance in distances:
        for i in range(2, distance):
            if distance % i == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors[i] = 1

    # Sort the factors by frequency
    factors = {k: v for k, v in sorted(factors.items(), key=lambda item: item[1], reverse=True)}

    return factors

# Read the ciphertext from a file
with open("Ctext-2.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')
    #convert to upper case
    ciphertext=ciphertext.upper()

# Determine the key length using Kasiski examination
factors = kasiski_examination(ciphertext)

# Print the most common factors
for factor, count in factors.items():
    print(factor, ":", count)




