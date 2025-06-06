# Ejercicio 1

for i in range(101):
    print(i)

# Ejercicio 2

numero = int(input("Ingrese un número entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    # Convertir a positivo para contar dígitos
    temp = abs(numero)
    while temp > 0:
        temp = temp // 10
        contador += 1

print(f"El número tiene {contador} dígitos.")

# Ejercicio 3

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

inicio = min(num1, num2) + 1
fin = max(num1, num2)
suma = 0

for i in range(inicio, fin):
    suma += i

print(f"La suma de los números entre {num1} y {num2} es: {suma}")

# Ejercicio 4

suma = 0
print("Ingrese números para sumar (0 para terminar):")

while True:
    numero = int(input())
    if numero == 0:
        break
    suma += numero

print(f"La suma total es: {suma}")

# Ejercicio 5

import random

numero_secreto = random.randint(0, 9)
intentos = 0

print("Adivina el número entre 0 y 9")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

# Ejercicio 6

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7

limite = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(limite + 1):
    suma += i

print(f"La suma de todos los números desde 0 hasta {limite} es: {suma}")

# Ejercicio 8

pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingrese 100 números enteros:")

for _ in range(100):
    num = int(input())
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Resultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# Ejercicio 9

suma = 0
cantidad = 100

print(f"Ingrese {cantidad} números enteros:")

for _ in range(cantidad):
    num = int(input())
    suma += num

media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")

# Ejercicico 10

numero = int(input("Ingrese un número entero: "))
invertido = 0
original = numero

# Convertir a positivo para el cálculo
numero = abs(numero)

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

# Aplicar signo si el original era negativo
if original < 0:
    invertido = -invertido

print(f"El número invertido es: {invertido}")