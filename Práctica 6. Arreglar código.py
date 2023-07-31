temperaturas = [300, 350, 400, 450, 500] #K
volumenes = [1, 2, 3, 4, 5] #L 
# Primer error, la lista de volumenes debe tener la misma longitud que la de temperaturas.
presiones = [1, 2, 3, 4, 5] #atm 
# Segundo error: el mismo que el primero.

R = 8.314 # J/mol*K
Na = 6.022e23 # Avogadro

energia_interna = 0 
# Tercer error: la energia interna debe inicializarse en cero.
i = 0 
# Cuarto error: i debe empezar en cero.

while i < len(temperaturas): 
    temperatura = temperaturas[i]
    volumen = volumenes[i] # Quinta error: j no está definido, debe ser i
    presion = presiones[i] # Sexto error: k no está definido, debe ser i

    #Calculamos la constante de los gases ideales
    k = R / Na # Septimo error: la constante k se calcula dividiendo R entre Na.

    #Calculamos la cantidad de moléculas
    n = (presion * volumen) / (R * temperatura) # Octavo error: falta un paréntesis al final.

    #Calculamos la energia interna
    u = n * R * temperatura
    energia_interna += u # Noveno error: se debe usar el operador += para acumular la energia interna.
    i += 1 # Decimo error: se debe incrementar i en uno.
print(energia_interna) 
