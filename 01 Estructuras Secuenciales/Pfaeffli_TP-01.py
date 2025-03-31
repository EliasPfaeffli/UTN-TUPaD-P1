# Ejercicio 1
print("¡Hola Mundo!")

# Ejercicio 2
nombre = input("Ingresa tu nombre:")

print(f"¡Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingresa tu nombre:")
apellido = input("Ingresa tu apellido:")
edad = input("Ingresa tu edad:")
lugarResidencia = input("Ingresa tu residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

#Ejercicio 4
import math
pi = math.pi
radio = float(input("Ingresa el radio del círculo:"))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#Ejercicio 5
segundos = float(input("Ingresa la cantidad de segundos:"))
horas = segundos / 3600

print(f"{segundos} equivalen a: {horas} hora/s.")

#Ejercicio 6
numero = int(input("Ingresa un número para generar la tabla de multiplicar: "))
cero = numero * 0 
uno = numero * 1 
dos = numero * 2 
tres = numero * 3
cuatro = numero * 4 
cinco = numero * 5
seis = numero * 6
siete = numero * 7 
ocho = numero * 8
nueve = numero * 9 
diez = numero * 10

print(f"{numero} * 0 = {cero}")
print(f"{numero} * 1 = {uno}")
print(f"{numero} * 2 = {dos}")
print(f"{numero} * 3 = {tres}")
print(f"{numero} * 4 = {cuatro}")
print(f"{numero} * 5 = {cinco}")
print(f"{numero} * 6 = {seis}")
print(f"{numero} * 7 = {siete}")
print(f"{numero} * 8 = {ocho}")
print(f"{numero} * 9 = {nueve}")
print(f"{numero} * 10 = {diez}")

#Ejercicio 7
num1 = float(input("Ingresa el primer número:"))
num2 = float(input("Ingresa el segundo número:"))

suma = num1 + num2
resto = num1 - num2
div = num1 / num2
multi = num1 * num2

print(f"{num1} + {num2} es: {suma}")
print(f"{num1} - {num2} es: {resto}")
print(f"{num1} / {num2} es: {div}")
print(f"{num1} * {num2} es: {multi}")

# Ejercicio 8 
altura = float(input("Ingresa tu altura:"))
peso = float(input("Ingresa tu peso:"))

imc = peso / (altura ** 2)

print(f"Tu IMC es {imc:.2f}")

#Ejercicio 9 
temp = float(input("Ingresa la temperatura en Celsius:"))
fahrenheit = temp * (9/5) + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit}")

#Ejercicio 10
num1 = float(input("Ingresa el primer número:"))
num2 = float(input("Ingresa el segundo número:"))
num3 = float(input("Ingresa el tercer número:"))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es: {promedio}")