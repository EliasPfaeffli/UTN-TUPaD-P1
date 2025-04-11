# Ejercicio 1
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 2
nota = int(input("Ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else: 
    print("Adulto/a")

# Ejercicio 5
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
from statistics import mode, median, mean
mi_lista = (1,2,5,5,3)
mean(mi_lista)
import random 
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(numeros_aleatorios)

# Ejercicio 7
string = input("Ingresa una palabra o frase: ")
if string and string[-1].lower() in 'aeiouáéíóúü':
    string += '!'
print(string)

# Ejercico 8
nombre = input("Ingresa tu nombre: ")
opcion = input("Elegi una opcion:\n1- Nombre mayuscula\n2- Nombre minuscula\n3- Como tiene que ser: ")

if opcion == "1":
    print(nombre.title())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else: 
    print("Debes elegir una opción.")

# Ejercicio 9
dato = float(input("Cual fue la magnitud del terremeto?: "))

if dato < 3:
    print("Muy leve")
elif dato >= 3 and dato < 4:
    print("Leve")
elif dato >= 4 and dato < 5:
    print("Moderado")
elif dato >= 5 and dato < 6:
    print("Fuerte")
elif dato >= 6 and dato < 7:
    print("Muy fuerte")
else:
    dato >= 7
    print("Extremo")

# Ejercicio 10
hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if hemisferio != 'N' and hemisferio != 'S':
    print("Error: Hemisferio no válido. Debe ser N o S.")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == 'N' else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == 'N' else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == 'N' else "Invierno"
    else:
        estacion = "Otoño" if hemisferio == 'N' else "Primavera"
    
    print(f"Estación actual: {estacion}")



    




