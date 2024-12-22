# 23. Simular el juego de "Piedra, papel o tijera".

print("==============================")
print("Juego piedra - papel - tijera.")
print("==============================")

print("Primer jugador")
print("--------------")
opcion = """1. Piedra
2. Papel
3. Tijera
"""
print(opcion)
primerJugador = int(input("Elige 1 - 3: "))

print("\nSegundo jugador")
print("----------------")
opcion = """1. Piedra
2. Papel
3. Tijera
"""
print(opcion)
segundoJugador = int(input("Elige 1 - 3: "))

if primerJugador == segundoJugador:
    print("Empate.")

elif (primerJugador == 1 and segundoJugador == 3) or (primerJugador == 2 and segundoJugador == 1) or (primerJugador == 3 and segundoJugador == 2):
    print("GANADOR - Primer jugador.")
else:
    print("GANADOR - Segundo jugador.")