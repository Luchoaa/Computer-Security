def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % key_length]
        
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char_index = alphabet.index(key_char)
            
            decrypted_char_index = (char_index - key_char_index) % 26
            decrypted_text += alphabet[decrypted_char_index]
        else:
            decrypted_text += char
    
    return decrypted_text

if __name__ == "__main__":
    ciphertext = "UFJKXQZQUNB"
    key = "SOLVECRYPTO"
    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("picoCTF{" + decrypted_text + "}")
