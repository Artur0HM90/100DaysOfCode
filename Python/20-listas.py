# 16. Generar una lista de números aleatorios.

import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]

print(numeros_aleatorios)