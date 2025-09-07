# Clasificación de triángulos:
# Solicita al usuario las 3 longitudes de los lados de un triángulo.
# Indica si es equilátero, isósceles o escaleno.

# Programa: Clasificación de triángulos

# longitudes de los lados al usuario
long1 = float(input('Escribe la longitud del primer lado: '))
long2 = float(input('Escribe la longitud del segundo lado: '))
long3 = float(input('Escribe la longitud del tercer lado: '))

# Verificar si los lados forman un triángulo válido
if (long1 + long2 > long3) and (long1 + long3 > long2) and (long2 + long3 > long1):
    # Clasificación de los triángulos según los lados
    if long1 == long2 == long3:
        print('El triángulo es equilátero')
    elif long1 == long2 or long1 == long3 or long2 == long3:
        print('El triángulo es isósceles')
    else:
        print('El triángulo es escaleno')
else:
    print('Los valores ingresados no forman un triángulo válido')
