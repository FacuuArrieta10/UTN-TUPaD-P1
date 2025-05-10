#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range

multiplos_de_4 = list(range(4,101,4))
print (multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

cinco_elementos = ([1,"boca",True,"Messi",10])
cuarto_elemento = cinco_elementos[3]
print (cuarto_elemento)

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
print(lista_vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

animales[1]=("loro")
animales[-1]=("oso")
print (animales)
#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7]
numeros.remove (max(numeros))
print(numeros)

#El programa crea una lista con una serie de números
#Luego llama a la lista y con remove va a eliminar un número de la misma.
#A través de la función max, elimina el número más grande.
#Luego muestra la lista por consola.


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros = list(range(10, 31, 5))  
print(numeros[:2])  

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["virtus", "hilux"]
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.


dobles = []                 
dobles.append(5 * 2)        
dobles.append(10 * 2)       
dobles.append(15 * 2)       

print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

# Lista inicial
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:


lista_anidada = [
    15,                     # lista_anidada[0]
    True,                   # lista_anidada[1]
    [25.5, 57.9, 30.6],     # lista_anidada[2][0], [2][1], [2][2]
    False                   # lista_anidada[3]
]

print(lista_anidada)