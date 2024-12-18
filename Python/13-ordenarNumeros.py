# 21. Ordenar una lista de números ingresados por el usuario.

listNumeros = []

ingresaCantidadNumero = int(input("Cuantos números vas ingresar: "))

for i in range(1, ingresaCantidadNumero + 1):
    ingresaNunmero = float(input(f"Ingresa {i} número: "))
    listNumeros.append(ingresaNunmero)
print(f"Lista de números: {listNumeros}")
#listNumeros.sort()   primer metodo
# print(f"Lista de números ordenados: {listNumeros}") primer metodo

print(f"Lista de números ordenados: {sorted(listNumeros)}") # segundo metodo