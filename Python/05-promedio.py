ingresaCantidadDeNotas = int(input("Ingresa cantidad de notas: "))

print("Ingresa las notas.")
promedio = 0
for i in range(1, ingresaCantidadDeNotas + 1):
    notas = float(input(f"{i}. Nota: "))
    promedio += notas
promedioFinal = promedio / ingresaCantidadDeNotas
print(f"Promedio final es: {promedioFinal}")