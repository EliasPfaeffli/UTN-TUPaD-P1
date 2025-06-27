# Ejercicio 1
multiplos_de_4 = list(range(4,101,4))
print(multiplos_de_4)

# Ejercicio 2
mi_lista = ["verde", "rojo", "negro", "azul", "blanco"]
print(mi_lista[-2])  # Usando indexación negativa (Imprime solo azul)

# Ejercicio 3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("!")
print(lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro" #Segundo elemento (Reemplaza "gato")
animales[-1] = "oso" #Ultimo elemento (Reemplaza pez)
print(animales)

# Ejercicio 5

# Crea una lista llamada numeros con valores [8, 15, 3, 22, 7].
# Con mas(numermos) encuentra el valor maximo de la lista (22).
# Elimina ese valor (22) de la lista usando remove.
# Imprime en pantalla la lista modificada sin el valor maximo [8, 15, 3, 7]

# Ejercicio 6
numeros = list(range(10, 31, 5))
print(numeros[:2]) #Muestra solo los dos primeros elementos

# Ejercicio 7
# Opcion 1
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Messi"
autos [2] = "DiMaria"
print(autos)

# # Opcion 2
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["ford", "chevrolet"]  # Reemplaza índices 1 y 2
print(autos)

# Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

# a) Agregar jugo al tercer cliente.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines".
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente.
compras[0].remove("pan")

# d) Imprimir lista resultante
print(compras)

# Ejercico 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)

