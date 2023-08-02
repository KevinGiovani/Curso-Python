"""
Bucles, numeros impares
Crea un script de Python que muestre los numeros impares tomando como
inicio y fin los numeros que le indique el usuario.
"""

__author__ = "Kevin G. Inzunza R"
__version__ = "1.0.0"

def ingresar_numeros():
    """
    Entrada de dos tipos de valores por medio de la terminal
    que serviran para crear una lista de numeros continuos

    Returns:
        list: Rango de inicio y final
    """
    inicio = int(input("Ingrese el valor del numero de inicio: "))
    final = int(input("Ingrese el valor del numero final: "))
    return [inicio, final]

def main(): 
    """
    Imprime en la terminal los valores que son impares a partir
    de la lista de numeros generada
    """
    print("Numeros impares")
    numeros = ingresar_numeros()
    lista = range(numeros[0],numeros[1]+1) # numeros[0] = inicio, numeros[1]= final
    impares = list(filter(lambda valor: valor%2!=0, lista)) # Función anonima que filtra los valores impares y los ingresa en una nueva lista
    print(f"Los numeros impares son: {impares}")
    
main()