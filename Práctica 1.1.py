#Escriba un programa que le solicite al usuario una cadena de caracteres en Mayúscula e imprima una lista con cada palabra en minúscula. Ayuda utilice métodos de la clase str

parrafo=input("Ingresa una frase o párrafo en mayúscula: ")
palabras=parrafo.split() #split() es un metodo va a dividir la frase o párrafo escrito y lo dividira en palabras para  imprimirlas en una lista.
palabras_minusculas=[palabra.lower() for palabra in palabras] #lower() es un meyodo que devuelve lo escrito los a minúscula
print("Lista con las palabras en minúsculas:", palabras_minusculas)

