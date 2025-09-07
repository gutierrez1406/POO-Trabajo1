# Programa: Conversor de calificaciones

calif = int(input("Escribe una calificación (0 - 100): "))

# Validar rango establecido
if 0 <= calif <= 100:
    if calif >= 90:
        print("Equivalencia: A")
    elif calif >= 80:
        print("Equivalencia: B")
    elif calif >= 70:
        print("Equivalencia: C")
    elif calif >= 60:
        print("Equivalencia: D")
    else:
        print("Equivalencia: F")
else:
    print("Error: La calificación debe estar entre 0 y 100.")
