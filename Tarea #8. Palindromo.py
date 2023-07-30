#Programa que compruebe el Palindromo

def palindromo(texto):
    texto = texto.replace(" ","")
    tamaño = len(texto)
    contador = 0
    for i in reversed(range(0, tamaño)):
        if texto[i].lower() != texto[contador].lower():
            return False
        contador += 1
    return True

while True:
    print("Comprobar Palindromo")
    print("Opciones:")
    print("1. Introducir un texto")
    print("2. Salir del programa")

    opcion = input("Elige una opción: ")
    if opcion == "1":
        texto = input("Ingrese un palindromo: ")
        texto_palindromo = palindromo(texto)
        if texto_palindromo ==True:
            print("El texto ingresado sí es un palindromo: ", texto)
        else:
            print("El texto ingresado no es un palindromo")
    elif opcion == "2":
        print("Gracias por usar la aplicación. ¡Hasta pronto!")
        break
