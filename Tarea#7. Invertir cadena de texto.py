#Programa para invertir cadenas de texto

texto=str(input("Ingrese una cadena de texto:"))
def invertir(texto):
    acumulador=" "
    for i in range(len(texto)):
        acumulador=texto[i]+acumulador
    print(acumulador)
invertir(texto)
