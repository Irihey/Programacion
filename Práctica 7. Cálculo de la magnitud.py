#Escriba un programa que calcule la magnitud de un terremoto a partir de los datos de una estación sismográfica. El programa debe:
	#Definir una función que reciba como parámetros la distancia epicentral en km y la amplitudes máxima y mínima en mm registradas en el sismograma.
	#Dentro de la función calcular la magnitud utilizando la f´ormula de Richter:
		
#M = log(A) + B log(d)

# M es la Magnitud.
# A es la amplitud máxima en mm.
# B es un coeficiente que depende de la variable d.
# d es la distancia epicentral en km

 	# La función debe retornar el valor de la magnitud calculada.
 	# En el programa principal, pedir al usuario los valores de distancia y amplitudes y llamar a la función para obtener la magnitud del sismo.
 	# Mostrar por pantalla la magnitud resultante.

"""
   { 3.5, if d ≤ 1km
B= {3, if 1km < d ≤ 10km
   {2, otherwise d ≥ 11km
"""

# Importando la librería 
import numpy as np
from math import log10

# Definir la función para calcular la magnitud del sismo
def magnitud_sismo(distancia, amplitud_maxima, amplitud_minima):
  
  # Determinar el valor de B según la distancia
  distancia=distancia*1000
  amplitud_maxima=amplitud_maxima/1000
  amplitud_minima=amplitud_minima/1000
  
  if distancia <= 1:
    coeficiente_b= 3.5
  elif 1< distancia <= 10:
    coeficiente_b= 3
  else:
    coeficiente_b= 2
    amplitud_total= abs((amplitud_maxima-amplitud_minima)/2)
    magnitud_m= np.log10(amplitud_total) + coeficiente_b * np.log10(distancia)

#Con libreria math
    magnitud_m1= log10(amplitud_total) + coeficiente_b *log10(distancia)

#Verificando que las dos librerias dan lo mismo valores 
  return [abs(magnitud_m), abs(magnitud_m1)]

distancia = float(input("Ingrese la distancia epicentral en km: "))
amplitud_maxima = int(input("Ingrese la amplitud máxima en mm: "))
amplitud_minima = int(input("Ingrese la amplitud mínima en mm: "))

# Llamamos a la función para obtener la magnitud del sismo
magnitud_final= magnitud_sismo(distancia, amplitud_maxima, amplitud_minima)

print("La magnitud del sismo es:" ,  magnitud_final)
