import time

# Define el alfabeto
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Lee el texto cifrado del archivo flag.txt
with open('flag.txt', 'r') as flag_file:
    encrypted_flag = flag_file.read().strip()

# Lee las posibles claves del archivo study-guide.txt
with open('study-guide.txt', 'r') as study_file:
    possible_keys = study_file.readlines()

# Función para descifrar texto
def decrypt(text, dictionary):
    decrypted = ''.join([dictionary[c] if c in dictionary else c for c in text])
    return decrypted

# Inicializa el contador y el tiempo de inicio
counter = 0
start_time = time.time()

# Itera sobre cada posible clave
for key in possible_keys:
    key = key.strip()  # Elimina los espacios en blanco y saltos de línea
    # Crea un diccionario de sustitución con la clave actual
    dictionary = dict(zip(key, alphabet))
    # Descifra el texto cifrado con la clave actual
    decrypted_flag = decrypt(encrypted_flag, dictionary)
    # Comprueba si el texto descifrado tiene sentido (por ejemplo, si contiene la palabra 'flag')
    if 'flag' in decrypted_flag:
        print("Found the key:", key)
        print("Decrypted Flag:", decrypted_flag)
        break
    # Incrementa el contador
    counter += 1
    # Si han pasado 30 segundos desde el último mensaje, imprime el progreso
    if time.time() - start_time >= 30:
        print(f"Checked {counter} keys so far...")
        start_time = time.time()
