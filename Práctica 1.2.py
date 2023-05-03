#Escriba un programa que le solicite al usuario 3 números enteros y de como resultado una lista con los valores ordenados. Ayuda utilice metodos de la clase list

enteros=[]
for x in range(3): #range() llena la lista con solo con la cantidad indicada en este caso solo seran 3 elementos
    valor=int(input("Ingrese un número:"))
    enteros.append(valor)  #append () añadira a la lista el número ingresado por el usuario
print(enteros)
enteros.sort() #El método .sort() ordena la lista de menor a mayor 
print("La lista ordenafa de menor a mayor: ", enteros)
enteros.sort(reverse=True)#.sort(reverse=True) ordena los elementos de la lista pero al revés de mayor a menor
print("La lista ordenada de mayor a menor: ", enteros)
