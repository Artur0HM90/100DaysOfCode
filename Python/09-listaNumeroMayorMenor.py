# 17. Programa para encontrar el número más grande y más pequeño en una lista.

listaNumeros = []
cantidadDeNumeros = int(input("Ingrese cuantos números vas ingresar: "))

for i in range (1, cantidadDeNumeros + 1):
    ingresarNumero = float(input(f"Ingresa {i}: "))
    listaNumeros.append(ingresarNumero)

print(f"La lista es: {listaNumeros}")
print(f"El número mayor es: {max(listaNumeros)}")
print(f"El número menor es: {min(listaNumeros)}")