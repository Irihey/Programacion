#En una fabrica de autopartes se realizar pruebas de resistencia a diferentes piezas producidas. Los resultados se tabulan en un vector
# (los resultados se dan en Kg de fuerzas soportadas antes de la ruptura)

# [R0 R1 R2 R3 R4 R5 R6 R7 ... Rn]

#Diseñe  un programa que le pida al usuario y valide los datos ingresados, ademas se requiere:
# Determinar la pieza con menor resistencia(falla más rapido). Esta sería la pieza defectuosa.
# Contar cuántas piezas soportaron una fuerza mayor a 300kg. Estas serían aptas para utilizarse en el modelo
# de automovil deseado.
# Calcular la media, mediana y moda de resistencia de las piezas.

# NOTA: no usar métodos de ordenamientos en pyhton (Ej:sort o sorted), deben ser creados por usted. Explique 
# brevemente  en un archivo file.txt el método



print("PROGRAMA PARA VERIFICAR LA RESISTENCIA DE UNA PIEZA\n") #\n es un carácter para indicar un salto de línea dentro de una cadena
piezas = int(input("Ingrese el número de piezas: "))
while piezas <= 0:
  print("El número debe ser positivo")
  piezas = int(input("Ingrese el número de piezas: "))

resultados = []

for i in range(piezas):
  vector_resultante = float(input(f"Ingrese el resultado de resistencia de la pieza {i+1}: "))
  while vector_resultante <= 0:
    print("El resultado debe ser positivo")
    vector_resultante = float(input(f"Ingrese el resultado de resistencia de la pieza {i+1}: "))
  resultados.append(vector_resultante)


# Luego, ordenamos los datos de forma ascendente y descendente usando un algoritmo de ordenamiento
# Usaremos el algoritmo de selección, que consiste en buscar el menor o mayor elemento y colocarlo al principio o al final de la lista

# Creamos una función para ordenar una lista en orden ascendente
def ordenar_ascendente(lista):
    for i in range(len(lista) - 1):
        minimo = i 
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j 
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

# Creamos una función para ordenar una lista en orden descendente
def ordenar_descendente(lista):
    for i in range(len(lista) - 1):
        maximo = i 
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[maximo]:
                maximo = j 
        lista[i], lista[maximo] = lista[maximo], lista[i]
    return lista

print("Vector resultante con los valores ingresados: ", resultados, "\n")

# Creamos copias de la lista original para ordenarlas sin modificarla
datos_ascendente = resultados.copy()
datos_descendente = resultados.copy()

# Ordenamos las copias usando las funciones creadas
datos_ascendente = ordenar_ascendente(datos_ascendente)
datos_descendente = ordenar_descendente(datos_descendente)

# Mostramos las listas ordenadas
print("DATOS ORDENADOS DE LAS FORMAS PEDIDAS\n")
print("Ordenados de forma ascendente:", datos_ascendente)
print("Ordenados de forma descendente:", datos_descendente)

# Después, determinamos la pieza con menor resistencia y contamos las piezas aptas para el modelo deseado
pieza_defectuosa = datos_ascendente[0]
print("\nLas piezas con menor resistencia son: ", pieza_defectuosa)

# Las piezas aptas son las que tienen una resistencia mayor a 300 kg
piezas_aptas = 0 
for i in resultados:
    if i >= 300:
        piezas_aptas += 1
print("Las piezas aptas para el modelo deseado son:", piezas_aptas)

print("\nCALCULO DE LA MEDIA, MEDIANA Y MODA\n")

# La media es el promedio de los valores
suma = 0 
for a in resultados:
    suma += a
media = suma / len(resultados) 
print("La media de resistencia de las piezas es:", media)

# La mediana es el valor central de la lista ordenada
# Si la lista tiene un número impar de elementos, la mediana es el elemento que está en la mitad
# Si la lista tiene un número par de elementos, la mediana es el promedio de los dos elementos centrales
# Usamos la lista ordenada de forma ascendente para hallar la mediana
elementos = len(resultados)
if elementos % 2 == 1: 
    mediana = datos_ascendente[elementos// 2] 
else: 
    mediana = (datos_ascendente[elementos // 2 - 1] + datos_ascendente[elementos // 2]) / 2 
print("La mediana de resistencia de las piezas es:", mediana)

# La moda es el valor más frecuente en la lista
# Usamos un diccionario para contar las frecuencias de cada valor
frecuencias = {} 
for b in resultados:
    if b in frecuencias:
        frecuencias[b] += 1 
    else: 
        frecuencias[b] = 1 

# Buscamos el valor con la mayor frecuencia en el diccionario
moda = None
maxima_frecuencia = 0 
for c in frecuencias: 
    if frecuencias[c] > maxima_frecuencia:
        moda = c
        maxima_frecuencia = frecuencias[c] 
        print("La moda de resistencia de las piezas es:", moda)
