def rot13(texto):
    resultado = ""
    for char in texto:
        if char.isalpha():
            desplazamiento = 13 if char.islower() else -13
            resultado += chr(((ord(char) - ord('a' if char.islower() else 'A')) + desplazamiento) % 26 + ord('a' if char.islower() else 'A'))
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    texto_cifrado = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
    texto_descifrado = rot13(texto_cifrado)
    print(texto_descifrado)
