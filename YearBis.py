# Programa: Verificar si un año es bisiesto

year = int(input("Escribe un año: "))

# Verificar si es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")
