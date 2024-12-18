# 9. Calcular el factorial de un número.
factorial = 1
print("======================")
print("Averigua el factorial.")
print("======================")

ingresaUnNumero = int(input("Ingresa un númro: "))
for i in range(1, ingresaUnNumero + 1):
    factorial *= i
print(f"El factorial de {ingresaUnNumero} es: {factorial}")