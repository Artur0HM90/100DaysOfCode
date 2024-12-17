# 12. Crear una agenda de contactos básica usando diccionarios.

agenda = {}
cuantosContactosIngresaras = int(input("Cuantos contactos vas a ingresar: "))
for i in range (1, cuantosContactosIngresaras + 1):
    nombre = str(input(f"Ingresa {i} nombre: "))
    telefono = int(input(f"Ingresa {i} número telefonico: "))
    agenda[nombre] = telefono

print("\nAgenda de contactos.")
print(agenda)