# 13. Validar si una cadena es un palíndromo. 

def es_palindromo(cadena):
    cadena_limpia = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())
    return cadena_limpia == cadena_limpia[::-1]


texto = "Anita lava la tina"
if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')