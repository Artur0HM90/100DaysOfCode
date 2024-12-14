# 22. Crear un conversor de unidades (km a millas, kg a libras, etc.)

opciones = """
1. Km a Millas
2. Km a Metros
3. Km a Centimetros
4. Km a Milimetros
5. Km a Micrometros
6. Km a Nanometro
7. Km a Yarda
8. Km a Pie
9. Km a Pulgada
10. Km a Milla nautica
11. Kilogramo a Libras
12. Kilogramo a Grama
13. Kilogramo a Miligramo
14. Kilogramo a Tonelado
15. Kilogramo a Onza
"""
print(opciones)
elegir = int(input("Elige entre 1 - 15: "))

while elegir < 1 or elegir > 15:
    if elegir < 1 or elegir > 15:
        print("ERROR - Debes ingresar del 1 - 15;")
        elegir = int(input("Elige entre 1 - 15: "))

if 1 <= elegir <= 10:
    kilometros = float(input("Ingresa el kilometraje: "))
    match elegir:
        case 1:
            print("Elegiste Km a Millas")
            resultado = kilometros * 0.621371
        case 2:
            print("Elegiste Km a Metros")
            resultado = kilometros * 1000
        case 3:
            print("Elegiste Km a Centimetros")
            resultado = kilometros * 100000
        case 4:
            print("Elegiste Km a Milimetros")
            resultado = kilometros * 1000000
        case 5:
            print("Elegiste Km a Micrometros")
            resultado = kilometros * 1e9
        case 6:
            print("Elegiste Km a Nanometro")
            resultado = kilometros * 1e12
        case 7:
            print("Elegiste Km a Yarda")
            resultado = kilometros * 1093.61
        case 8:
            print("Elegiste Km a Pie")
            resultado = kilometros * 3280.84
        case 9:
            print("Elegiste Km a Pulgada")
            resultado = kilometros * 39370.1
        case 10:
            print("Elegiste Km a Milla nautica")
            resultado = kilometros * 0.539957
else:
    kilogramos = float(input("Ingresa los kilogramos: "))
    match elegir:
        case 11:
            print("Elegiste Kilogramo a Libras")
            resultado = kilogramos * 2.20462
        case 12:
            print("Elegiste Kilogramo a Grama")
            resultado = kilogramos * 1000
        case 13:
            print("Elegiste Kilogramo a Miligramo")
            resultado = kilogramos * 1e6
        case 14:
            print("Elegiste Kilogramo a Tonelado")
            resultado = kilogramos / 1000
        case 15:
            print("Elegiste Kilogramo a Onza")
            resultado = kilogramos * 35.274

print(f"El resultado es: {resultado}")
    
