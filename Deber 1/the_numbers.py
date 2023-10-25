def descifrar_mensaje(secuencia_numeros):

    mensaje_descifrado = "picoCTF{"
    
    for numero in secuencia_numeros:

        letra = chr(numero + ord('a') - 1) 
        mensaje_descifrado += letra
    
    mensaje_descifrado += "}"
    
    return mensaje_descifrado


if __name__ == "__main__":

    secuencia_numeros = [20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
    
    mensaje_descifrado = descifrar_mensaje(secuencia_numeros)
    print(mensaje_descifrado)
