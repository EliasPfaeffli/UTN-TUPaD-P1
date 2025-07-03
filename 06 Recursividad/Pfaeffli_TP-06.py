# Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

# Mostrar factoriales desde 1 hasta n
n = int(input("Ingrese un número entero positivo: "))
for i in range(1, n + 1):
    print(f"Factorial de {i}: {factorial(i)}")

# Ejercicio 2

def fibonacci(pos):
    if pos == 0:  
        return 0
    elif pos == 1:  
        return 1
    else:  
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la posición hasta la que desea ver la serie: "))
for i in range(n + 1):
    print(f"Posición {i}: {fibonacci(i)}")

# Ejercico 3

def potencia(base, exp):
    if exp == 0:
        return 1
    else:  
        return base * potencia(base, exp - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4

def decimal_a_binario(n):
    if n == 0:  
        return "0"
    elif n == 1:  
        return "1"
    else:  
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1: 
        return True
    elif palabra[0] != palabra[-1]:  
        return False
    else:
        return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ").lower()
print(f"¿'{texto}' es palíndromo? {es_palindromo(texto)}")

# Ejercicio 6

def suma_digitos(n):
    if n < 10: 
        return n
    else: 
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print(f"Suma de dígitos de {numero}: {suma_digitos(numero)}")

# Ejercicio 7

def contar_bloques(n):
    if n == 1: 
        return 1
    else:  
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques en la base: "))
print(f"Bloques totales necesarios: {contar_bloques(niveles)}")

# Ejercicio 8

def contar_digito(numero, digito):
    if numero < 10: 
        return 1 if numero == digito else 0
    else:  # Caso recursivo
        ultimo = numero % 10
        resto = numero // 10
        return (1 if ultimo == digito else 0) + contar_digito(resto, digito)

num = int(input("Ingrese un número entero positivo: "))
d = int(input("Ingrese un dígito a buscar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}")
