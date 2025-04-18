#1.Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal

#Definición de funciones

# Definición de funciones
def imprimir_hola_mundo():
    print("Hola mundo!")

# Función principal
imprimir_hola_mundo()


#2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Definición de funciones
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

# Función principal
saludar_usuario(input("Ingrese su nombre:"))

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de funciones
def informacion_personal(nombre,apellido,residencia,edad):
     print(f"Hola soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")

# Función principal

nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su residencia: ")

informacion_personal(nombre_usuario, apellido_usuario,residencia_usuario,edad_usuario)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi
# Definición de funciones

def calcular_area_circulo (radio):
    area= (pi * float(radio) ** 2)
    print (f"El área del círculo es: {area}")

def calcular_perimetro_circulo (radio):
    perimetro=(2 * pi * float(radio))
    print (f"El perimetro del círculo es {perimetro} ")


# Función principal

radio = float(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)




#5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

# Definición de funciones

def segundos_a_horas(segundos):
    minutos = int(segundos) // 60
    hora = int(minutos) // 60
    print (f"La cantidad de horas correspondientes es: {hora}")

# Función principal

segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones

def tabla_multiplicar(numero): 
    for i in range (1,11):
        tabla = numero * i
        print(f"{numero} x {i} = {tabla}") 

# Definición de funciones

numero = int(input("Ingrese un número por favor: "))
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Definición de funciones
from tabulate import tabulate

def operaciones_basicas (a, b):
    division = a // b
    multiplicacion = a * b
    suma = a + b
    resta = a - b
 # Creamos la tabla para mostrar los resultados
    tabla = [
        ["Suma", suma],
        ["Resta", resta],
        ["Multiplicación", multiplicacion],
        ["División", division],
    ]
    # Imprimimos la tabla usando tabulate
    print(tabulate(tabla, headers=["Operación", "Resultado"]))
    # Devolvemos la tupla con los resultados (opcional si solo quieres imprimir)
    return suma, resta, multiplicacion, division


# Funcion principal


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
operaciones_basicas(a,b)


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definición de funciones

def calcular_imc(peso, altura):
    IMC = round(float(peso) / float(altura) ** 2)
    print (f"Tu IMC es de: {IMC}")


# Función principal

peso= input("Ingrese su peso en kg: ")
altura= input("Ingrese su altura en metros: ")
calcular_imc(peso,altura)


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Definición de la función
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de grados Celsius a grados Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Función principal
celsius_temp = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit_temp = celsius_a_fahrenheit(celsius_temp)
print(f"{celsius_temp} grados Celsius son equivalentes a {fahrenheit_temp} grados Fahrenheit.")
    

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

