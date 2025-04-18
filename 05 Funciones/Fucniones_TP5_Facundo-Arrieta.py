# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Definición de la función
def calcular_promedio(a, b, c):
    """Calcula el promedio de tres números."""
    promedio = (a + b + c) / 3
    return promedio

# Función principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio_resultado = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio_resultado}")