#1)	Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#* Se pide edad.
edad_usario= int(input("Ingrese su edad: "))

#* Si el usario es mayor a 18, se muestra que es mayor.
if (edad_usario > 18):
    print ("Es mayor de edad")


#2)	Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.


#* Se pide nota.
nota_usuario= int(input("Ingrese su nota: "))

#Si es mayor a 6 da aprobado, si no da desaprobado.
if nota_usuario > 6:
    print ("Aprobado")
else: 
    print ("Desaprobado")


#3)	Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
#  en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.


#* Pedir un número.
numero= int(input("Ingrese un número: "))

#*Se comprueba si es par o impar
if numero % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print ("Por favor ingrese un número par")


#4)	Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#	Niño/a: menor de 12 años.
#	Adolescente: mayor o igual que 12 años y menor que 18 años.
#	Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#	Adulto/a: mayor o igual que 30 años.


#*Pedimos la edad:

edad=int(input("Ingrese su edad: "))

#*Según su edad la categoria:

if edad < 12: 
    print ("Eres niño/a")
elif edad >= 12 and edad < 18:
    print("Eres adolescente")
elif edad >= 18 and edad < 30:
    print("Eres adulto/a joven")
elif edad >= 30:
    print("Eres adulto/a mayor")
    

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

#*pedimos contraseña

contraseña= (input("Ingrese su contraseña: "))

longitud= len(contraseña)

#*Verificamos contraseña
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
import statistics

#* Generamos la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#*Calculamos media, mediana y moda
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

#* Mostramos los valores
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

#* Determinamos el sesgo
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")


#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#*Pedimos palabra o frase.
palabra= (input("Ingrese una frase o palabra: "))

#*Utuilizamos .lower() para comprobar que la palabra o frase termina en vocal.
ultima_vocal= palabra.lower().endswith(("a","e","i","o","u"))

#*Mostramos por pantalla la palabra o frase + ! si termina en vocal,caso contrario solo la palabra o frase.
if ultima_vocal:
    print(palabra +"!")
else:
    print(palabra)

 

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 

#*Pedir al usario que ingrese su nombre
nombre=(input("Ingresa tu nombre: "))

#*Pedir numero 

print("Si quieres tu nombre en mayúsculas ingresa 1")
print("Si quieres tu nombre en minisculas ingresa 2")
print("Si quieres tu nombre con la primera letra en mayúscula ingresa 3")
numero= (int(input("Ingresa un número: ")))

#*Según número hacer:
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())


#9)Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 


#*Pedir magnitud del terremoto:
magnitud= (int(input("Ingrese la magnitud del terremoto: ")))

#*Según magnitud hacer:
if magnitud < 3:
    print("Muy leve(Imperceptible.)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve(ligeramente perceptible.)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado(sentido por personas, pero generalmente no causa daño.)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles.)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte(puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo(puede causar graves daños a gran escala)")


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

def obtener_estacion(hemisferio, mes, dia):
    if mes == 12 and dia >= 21 or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif mes == 3 and dia >= 21 or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif mes == 6 and dia >= 21 or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif mes == 9 and dia >= 21 or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        return "Fecha no válida"

    return estacion_norte if hemisferio.upper() == "N" else estacion_sur

#* Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip()
mes = int(input("¿Qué mes es? (en número, ej. 4 para abril): "))
dia = int(input("¿Qué día es? (número del día): "))

#*Obtener e imprimir estación
estacion = obtener_estacion(hemisferio, mes, dia)
print(f"La estación del año es: {estacion}")