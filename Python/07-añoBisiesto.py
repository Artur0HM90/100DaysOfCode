# 14. Determinar si un año es bisiesto.

ingreseYear = int(input("Ingrese un año: "))
if (ingreseYear  % 4 == 0) and ( ingreseYear % 100 != 0 or ingreseYear % 400 == 0):
    print(f"El año {ingreseYear} es bisiesto.")

else:
    print(f"El año {ingreseYear} no es bisiest0.")