def rot13(texto):
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            desplazamiento = 13 if char.islower() else -13
            resultado += chr(((ord(char) - ord('a' if char.islower() else 'A') + desplazamiento) % 26) + ord('a' if char.islower() else 'A'))
        else:
            resultado += char
    
    return resultado

mensaje_cifrado = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
mensaje_descifrado = rot13(mensaje_cifrado)

print(mensaje_descifrado)
