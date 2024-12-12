# 5. Convertir temperaturas entre Celsius y Fahrenheit.
print("\n===========================")
print("Conversión de temperaturas.")
print("===========================")

opcion ="""
1. Celsius a Fahrenheit
2. Fahrenheit a Celsius
"""
print(opcion)
elegir = int(input("Elige 1 - 2: "))

while elegir < 1 or elegir > 2:
    if elegir < 1 or elegir > 2:
        print("ERROR - Debes ingresar 1 - 2.")
        elegir = int(input("Elige 1 - 2: "))


match elegir:
    case 1:
        ingresaCelsius = float(input("Ingresa temperatura en Celsius: "))
        formula = (ingresaCelsius * 9/5) + 32
        print (f"Celsius a Fahrenheit: {formula} grados Fahrenheit.")
    case 2:
        ingresaFahrenheit = float(input("Ingresa temperatura en Fahrenheit: "))
        formula2 = (ingresaFahrenheit - 32) * 5/9
        print(f"Fahrenheit a Celsius: {formula2} grados Celsius.")
