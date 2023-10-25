def cesar_descifrar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - offset - desplazamiento) % 26 + offset)
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    texto_cifrado = "dspttjohuifsvcjdpoabrkttds"
    for desplazamiento in range(1, 26):
        texto_descifrado = cesar_descifrar(texto_cifrado, desplazamiento)
        print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")
