# 6. Crear un cronómetro simple.

import time

print("============")
print("CRONOMETRO.")
print("============")

input("Presione 'Enter' para comenzar.")
inicio = time.time()
print("Cronómetro iniciando...")

print("Presiona 'Ctrl+C' para detenerlo.")

try:
    while True:
        transcurrido = time.time() - inicio
        horas = int(transcurrido // 3600)
        minutos = int((transcurrido % 3600) // 60)
        segundos = transcurrido % 60
        print(f"Tiempo transcurrido: {horas} horas, {minutos} minutos y {segundos:.2f} segundos.", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCronómetro detenido.")