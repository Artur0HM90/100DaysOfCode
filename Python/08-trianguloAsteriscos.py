# 24. Generar un patrón de triángulo con asteriscos.

ingreseAsteristos = int(input("Ingresa cantidad de asteristos: "))
for i in range(1, ingreseAsteristos + 1):
    for j in range (i):
        print("*", end="")
    print()