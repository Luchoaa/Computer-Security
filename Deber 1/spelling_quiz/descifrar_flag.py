import random

# Define the substitution cipher key
key = 'xunmrydfwhglstibjcavopezqk'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dictionary = dict(zip(key, alphabet))

# Function to encrypt text
def encrypt(text):
    encrypted = ''.join([dictionary[c] if c in dictionary else c for c in text])
    return encrypted

# Read the flag from flag.txt
with open('flag.txt', 'r') as flag_file:
    flag = flag_file.read().strip()

# Encrypt the flag
encrypted_flag = encrypt(flag)
print("Encrypted Flag:", encrypted_flag)