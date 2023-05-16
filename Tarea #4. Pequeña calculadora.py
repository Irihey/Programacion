#Hacer un programa que sume dos numeros y asegurar que el texto que ingrese el usuario se pueda trasnformar a número

numeros_a_letras = {0:"cero", 1:"uno", 2:"dos",3:"tres", 4:"cuatro", 5:"cinco", 6:"seis", 7:"siete", 8:"ocho", 9:"nueve", 10:"diez"}
letras_a_numeros = {"cero":0, "uno":1, "dos":2,"tres":3, "cuatro":4, "cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9, "diez":10}

numero = input("Introduce un número o número en letras del 1 al 10: ")

if numero.isdigit():
    numero = int(numero)
    if numero in numeros_a_letras:
        print(numeros_a_letras[numero])
else:
    if numero in letras_a_numeros:
        print(letras_a_numeros[numero])
        numero_1=float(letras_a_numeros[numero])
        
letra = input("Introduce una letra o letra en números del 1 al 10: ")

if letra.isdigit():
    letra = int(letra)
    if letra in numeros_a_letras:
        print(numeros_a_letras[letra])
else:
    if letra in letras_a_numeros:
        print(letras_a_numeros[letra])
        numero_2=float(letras_a_numeros[letra])

suma=numero_1+numero_2
print(suma)
