#Realizar una rutina en la que dado dos números escritos en base dos (también conocida como notación binaria) los sume respetando las siguientes limitaciones : 
#1. Los números deben ser almacenados en vectores.
#2. consideré números no más de diez (10) dígitos binarios.
#3. Tome en cuenta que no necesariamente los dos números poseen la misma cantidad de dígitos.


#Ingresamos los numeros binarios
numero_binario1 = int(input("Ingrese el primer número:  "))
numero_binario2 = int(input("Ingrese el segundo número: "))

#Verificamos si son binarios
binario = True 
variable_1 = numero_binario1 
while variable_1 > 0 and binario:
    resta = variable_1 % 10 
    division = variable_1 // 10 
    if (resta == 0) or (resta == 1): 
        variable_1 = division 
    else: 
        print(str(variable_1), "El primer número ingresado no es binario")
        binario = False 

variable_1 = numero_binario2
while variable_1 > 0 and binario:
    resta = variable_1 % 10
    division = variable_1 // 10
    if (resta == 0) or (resta == 1):
        variable_1 = division
    else:
        print(str(variable_1), "El segundo número ingresado no es binario")
        binario = False

#Si son binarios, se procede hacer la suma
if binario:
    acumulador = 0 
    suma = 0 
    multiplicacion = 1 
    while numero_binario1 > 0 or numero_binario2 > 0 or acumulador > 0: 
        ultimo_digito_1 = numero_binario1 % 10 # último dígito de numero_binario1
        ultimo_digito_2 = numero_binario2 % 10 # último dígito de numero_binario2
        numero_binario1 = numero_binario1 // 10
        num_binario2 = numero_binario2 // 10 
        suma_binaria = ultimo_digito_1 + ultimo_digito_2 + acumulador 
        acumulador = suma_binaria // 2 
        suma_binaria = suma_binaria % 2 
        suma = suma_binaria * multiplicacion + suma 
        multiplicacion = multiplicacion * 10 
    print("La suma de ambos números es: ", str(suma)) 
