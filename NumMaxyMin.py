# Programa: Comparación de tres números

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
num3 = float(input("Escribe el tercer número: "))

# Determinar el mayor y el menor usando funciones de Python
mayor = max(num1, num2, num3) # encuentra el valor mayor
menor = min(num1, num2, num3) # encuentra el valor menor

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
