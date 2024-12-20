# 10. Programa para imprimir los primeros N números de Fibonacci.

ingresarNumero = int(input("Ingresa un número: "))

if ingresarNumero <= 0:
    print("El número debe ser mayor a cero.")
else:
    a, b = 0, 1
    print("Secuencia de Fibonacci.")
    for i in range(ingresarNumero):
        print(a, end=" ")
        a, b = b, a + b
