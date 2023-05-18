#Desarrollar un programa que permita realizar las 4 operaciones  básicas (suma, resta, multiplicacion y division). El programa debe permitir validar el tipo y el valor correcto de los datos ingresados por el usuario en caso de haber un error manejarlos con los visros en clase.

#En un archivo adjunto se explicara el uso del operador AND e IN, además de del uso "."

numero_1 = input("Introduce el primer número: ")
numero_2 = input("Introduce el segundo número: ")

if numero_1.isnumeric() and numero_2.isnumeric: 
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
elif"." in numero_1 and "." in numero_2: 
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
elif numero_1.isnumeric() and "."in numero_2: 
    numero_2 = float(numero_2)
elif"." in numero_1 and numero_2.isnumeric(): 
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
else:
    raise ValueError("Los valores introducidos no son correctos, ingrese solo números.")
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicar = numero_1 * numero_2
if numero_2 == 0:
        raise ValueError("El segundo número no puede ser cero.")
division = numero_1 / numero_2
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicar)
print("La división es:", division)