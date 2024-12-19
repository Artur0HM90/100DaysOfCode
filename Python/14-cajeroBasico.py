# 15. Simular un cajero automático básico.

cuenta = 2500
opciones = """
1. Ver cuenta.
2. Retirar.
3. Depositar.
"""
print(opciones)
elegir = int(input("Elige 1 - 3: "))
while elegir < 1 or elegir > 3:
    if elegir < 1 or elegir > 3:
        print("ERROR - Debes ingresar del 1 - 3.")
        elegir = int(input("Elige 1 - 3: "))


match elegir:
    case 1:
        cuenta
    case 2:
        retirarDinero = float(input("Cuantos vas a retirar: "))
        if retirarDinero > cuenta:
            print(f"Saldo insuficiente.")
        else:
            cuenta -= retirarDinero
    case 3:
        depositarDinero = float(input("Cuantos vas a depositar: "))
        cuenta += depositarDinero
print(f"En tu saldo tienes: S/{cuenta:.2f} soles.")