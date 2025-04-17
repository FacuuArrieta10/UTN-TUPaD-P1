
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 10 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

i=0
for i in range (1,101,1):
    print(i)



#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

#*Pedimos número:

nEntero = input("Ingrese un número: ")

#* Elimina el signo negativo si lo hubiera
if nEntero.startswith('-'):
    nEntero = nEntero[1:]

#* Verifica que el número ingresado es válido
if nEntero.isdigit():
    cantidad_digitos = len(nEntero)
    print("El número tiene", cantidad_digitos, "dígito(s).")
else:
    print("No ingresó un número entero válido.")



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores  
# dados por el usuario, excluyendo esos dos valores. 

#* Solicita dos valores enteros al usuario
inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))

#* Asegura que inicio sea el menor y fin el mayor
menor = min(inicio, fin)
mayor = max(inicio, fin)

#* Suma los números entre los dos (excluyendo los límites)
suma = 0
for i in range(menor + 1, mayor):
    suma += i

#* Muestra el resultado
print("La suma de los números entre", menor, "y", mayor, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.

acumulador = 0
numero = int(input("Ingrese un número: "))
while numero != 0:
    acumulador = acumulador + numero
    numero = int(input("Ingrese otro número para continuar, o ingrese 0 para terminar de sumar: "))
print ("EL total acomulado es:",acumulador)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 


import random  #* Importamos el módulo random para generar números aleatorios

#* Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)

#* Inicializamos el contador de intentos
intentos = 0
acertado = False

#* Iniciamos el juego
print("Adivina el número entre 0 y 9.")

#* Bucle para que el usuario siga intentando hasta acertar
while acertado == False:
    intento = int(input("Adivina el número: "))  # Pedimos un número al usuario
    intentos += 1  # Aumentamos el contador de intentos
    
    if intento == numero_aleatorio:
        acertado = True  # Si el usuario acierta, cambiamos acertado a True
        print(f"¡Felicidades! Has acertado el número en {intentos} intentos.")

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

n_pares=100


for n_pares in range (100,-1,-2):
    
    print(n_pares)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.


numero= int(input("Ingrese un número: "))
acumulador=int(0)

for i in range (0,numero+1):
    acumulador += i
print(acumulador)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

n_pares = 0
n_impares = 0
n_negativos = 0
n_positivos= 0

for i in range (1,101):
    numero=int(input("Ingrese un número: "))
    if numero % 2 == 0:
        n_pares += 1
    else: n_impares += 1
    if numero < 0:
        n_negativos += 1
    else: n_positivos += 1

print("Cantidad de números pares",n_pares)
print("Cantidad de números impares",n_impares)
print("Cantidad de números positivos",n_positivos)
print("Cantidad de números negativos",n_negativos)


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

numero= 0
acumulador= 0
contador= 0
media= 0

for i in range (1,4):
    numero=int(input("Ingrese un número: "))
    acumulador += numero
    contador += 1

media = acumulador / contador

print (media)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 


numero = input("Ingrese un número: ")

#*Verificamos si es un número válido (entero positivo o negativo)
if numero.lstrip('-').isdigit():
    #*Invertimos el string (y dejamos el signo si existe)
    if numero.startswith('-'):
        invertido = '-' + numero[1:][::-1]
    else:
        invertido = numero[::-1]
    
    print("Número invertido:", invertido)
else:
    print("Entrada inválida. Ingrese un número entero.")