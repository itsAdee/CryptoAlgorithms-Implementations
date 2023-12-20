import string

def generate_key(plaintext, key):
    """Generates a key for the Vigenere cipher"""
    key = list(key)
    if len(plaintext) == len(key):
        return(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def vigenere_decode(ciphertext, key):
    """Decodes a Vigenere ciphertext using a given key"""
    plaintext = ""
    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plaintext += chr(x)
    return plaintext

# Read the ciphertext from a file
with open("Ctext-2.txt", "r") as file:
    ciphertext = file.read().replace('\n', '')

#create a list storing indexes at which there are spaces
spaces = [i for i, x in enumerate(ciphertext) if x == " "]
#convert cipher text to upercase and remove all non aplhabetecial characters
ciphertext = ciphertext.upper()
ciphertext = ''.join([i for i in ciphertext if i in string.ascii_uppercase])

# Generate a key
key = generate_key(ciphertext, "BRUSH")

# Decode the ciphertext
plaintext = vigenere_decode(ciphertext, key)
#INSERT THE SPACES BACK
for i in spaces:
    plaintext = plaintext[:i] + ' ' + plaintext[i:]
    


print(plaintext)
