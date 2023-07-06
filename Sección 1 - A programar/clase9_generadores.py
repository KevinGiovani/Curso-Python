# Generadores
def impares():
    for numero in range(1,50,2):
        yield numero #Yield pausa la ejecución de la función hasta que la vuelva a llamar (se guarda su estado)

print(impares())  #Visualización en terminal de que se creo un generador (No muestra resultados)

generador1 = impares()
#Forma 1 con for
for numero in generador1:
    print(numero)

generador2 = impares()
#Forma 2 con next (uno a uno)
print(next(generador2))
print(next(generador2))
print(next(generador2))