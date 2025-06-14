# 1) Función recursiva para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Pedimos al usuario el número máximo
limite = int(input("Ingrese un número: "))
for i in range(1, limite + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# 2) Función recursiva para calcular Fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario la cantidad de términos
cantidad = int(input("Ingrese hasta qué término de la serie de Fibonacci desea ver: "))
for i in range(cantidad + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# 3) Función recursiva para calcular potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Probamos la función
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

# 4) Conversión de decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Probamos la función
numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")

# 5) Función recursiva para verificar si es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Probamos la función
palabra = input("Ingrese una palabra: ").lower()
print(f"¿Es palíndromo? {es_palindromo(palabra)}")

# 6) Suma de los dígitos recursivamente
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Probamos la función
numero = int(input("Ingrese un número: "))
print(f"La suma de sus dígitos es: {suma_digitos(numero)}")

# 7) Contar bloques de una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Probamos la función
nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

# 8) Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

# Probamos la función
numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese el dígito a buscar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
