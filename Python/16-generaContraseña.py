# 3. Crear un generador de contraseñas aleatorias.

import random
import string

texto = int(input("Ingresa la longitud de la contraseña: "))
letras = string.ascii_letters + string.digits + string.punctuation

contraseña = ""
for _ in range(texto):
    contraseña += random.choice(letras)

print(f"Tu contraseña aleatoria es: {contraseña}")