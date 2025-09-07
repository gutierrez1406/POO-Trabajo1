# Programa: Tarifa de entrada a un parque

edad = int(input("Escribe tu edad: "))

# Determinamos la tarifa según la edad
if edad < 12:
    print("El costo de la entrada es: $50")
elif 12 <= edad <= 17:
    print("El costo de la entrada es: $80")
elif edad >= 18:
    print("El costo de la entrada es: $120")
else:
    print("Edad inválida")
