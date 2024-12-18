# 7. Generar una tabla de multiplicar de un número ingresado por el usuario.

ingresaNumero = int(input("Ingesa que tabla quieres saber: "))
for i in range(1, 12 + 1):
    print(f"{ingresaNumero} x {i} = {ingresaNumero * i}")