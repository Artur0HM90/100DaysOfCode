# 6. Crear un cronómetro simple.

import time

print("============")
print("CRONOMETRO.")
print("============")

input("Presione 'Enter' para comenzar.")
inicio = time.time()
print("Cronómetro iniciando...")

input("\nPresione 'Enter' para detener.")
fin = time.time()

transcurrido = fin - inicio

horas = int(transcurrido // 3600)
minutos = int((transcurrido % 3600) // 60)
segundos = transcurrido % 60

print(f"Tiempo transcurrido: {horas} horas, {minutos} minutos y {segundos:2F} segundos.")