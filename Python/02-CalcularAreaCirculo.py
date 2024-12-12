# 2. Programa para calcular el área de un círculo dado su radio.

ingresaRadio = float(input("Ingresa radio del circulo: "))
PI = 3.1416

#solucion = PI * (ingresaRadio ** 2) primera forma 
solucion = PI * (pow(ingresaRadio, 2)) # segunda forma
print(f"El area del circulo es: {solucion}")