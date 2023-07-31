#Alquiler, el famoso guerrero griego, entabla una carrera con una tortuga a la cual le da x metros de ventaja. la tortuga se desplaza a una velocidad v metros por 
#hora y aquiles es diez veces más veloz que ella. Diseñe un programa que simule la carrera y genere como resultado el tiempo en horas, minutos, y segundos que tarda 
#aquiles en alcanzar a la tortuga, los 5 datos tabulados de coordenadas distancia y tiempo de Aquiles hasta alcanzar a la tortuga.

print("Ingresa los siguientes valores pedidos:")
print("LA VENTAJA DEBE SER EN METROS Y LA VELOCIDAD EN METROS POR HORA")
x = float(input("La ventaja de la tortuga: "))
v = float(input("La velocidad de la tortuga: "))

distancia_de_la_tortuga = x
distancia_de_aquiles = 0
velocidad_de_la_tortuga = v
velocidad_de_aquiles = 10 * v
tiempo_en_segundos = 0

coordenadas = []

while distancia_de_aquiles <= distancia_de_la_tortuga:
    distancia_de_la_tortuga -= velocidad_de_la_tortuga 
    distancia_de_aquiles += velocidad_de_aquiles 
    tiempo_en_segundos += (distancia_de_la_tortuga/velocidad_de_aquiles)

    coordenadas.append([distancia_de_aquiles, tiempo_en_segundos])

horas = int(tiempo_en_segundos / 3600)
minutos = int((tiempo_en_segundos % 3600) / 60)
segundos = int(tiempo_en_segundos % 60)

print("Aquiles tarda", horas, "horas,", minutos, "minutos y", segundos, "segundos en alcanzar a la tortuga.")
    
print("\nDistancia\tTiempo")
for i, coordenada in enumerate(coordenadas): #La función enumerate() se utiliza para iterar sobre una lista y devolver tanto el índice como el valor de cada elemento de 
                                             #la lista. En el código que proporcionó, la función enumerate() se utiliza para iterar sobre la lista coordenadas y devolver 
                                             #tanto el índice como el valor de cada elemento de la lista. La variable i contiene el índice del elemento actual y la variable 
                                             #coordenada contiene el valor del elemento actual.
    if i < 5:
        print("{:.2f} m\t\t{}:{}:{}".format(coordenada[0], int(coordenada[1] / 3600), int((coordenada[1] % 3600) / 60), int(coordenada[1] % 60)))
#La cadena "{:.2f} m\t\t{}:{}:{}" es una cadena de formato que se utiliza para imprimir los datos de la carrera en una tabla. El primer elemento {:.2f} es un número decimal 
#con dos decimales que representa la distancia recorrida por Aquiles. El segundo elemento \t\t es un tabulador que se utiliza para separar la distancia y el tiempo. Los 
# siguientes tres elementos {} son números enteros que representan las horas, minutos y segundos que tarda Aquiles en alcanzar a la tortuga.
