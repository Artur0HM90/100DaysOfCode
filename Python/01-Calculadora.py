# 1. Calculadora básica (suma, resta, multiplicación, división).

opcion = """
1. Suma
2. Resta.
3. Multiplicación.
4. División.
"""
print(opcion)
elegir = int(input("Elige entre el 1 - 4: "))

while elegir < 1 or elegir > 4:
    if elegir < 1 or elegir > 4:
        print ("ERROR - Debes elegir entre 1 - 4.")
        elegir = int(input("Elige entre el 1 - 4: "))

primerNumero = float(input("Ingresa primer número: "))
segundoNumero = float(input("Ingresa segundo número: "))

match elegir:
    case 1:
        resultado = primerNumero + segundoNumero
    case 2: 
        resultado = primerNumero - segundoNumero
    case 3:
        resultado = primerNumero * segundoNumero
    case 4:
        if segundoNumero == 0:
            print("No se puede dividir por cero.")
            resultado = 0
        else:
            resultado = primerNumero / segundoNumero

print(f"El resultado es: {resultado}")

