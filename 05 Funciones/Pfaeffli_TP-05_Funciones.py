# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600

seg = float(input("Ingrese los segundos: "))
print(f"{seg} segundos equivalen a {segundos_a_horas(seg):.2f} horas")

# Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Ingrese la temperatura en Celsius: "))
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C equivalen a {temp_f:.1f}°F")

# Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))
prom = calcular_promedio(num1, num2, num3)
print(f"El promedio es: {prom:.2f}")

