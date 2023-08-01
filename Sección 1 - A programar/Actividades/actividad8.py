"""
Bucles, numeros pares mostrados en orden inverso
Crea un script que pregunte al usuario numero inicial y final y muestre los numeros pares que se
incluyen dentro del intervalo mostrandolos en orden inverso.
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
    Imprime en la terminal los valores de mayor a menor que son pares a partir
    de la lista de numeros generada 
    """
    print("Numeros impares")
    numeros = ingresar_numeros()
    lista = range(numeros[0],numeros[1]+1) # numeros[0] = inicio, numeros[1]= final
    pares = list(filter(lambda valor: valor%2==0, lista)) # Función anonima que filtra los valores pares y los ingresa en una nueva lista
    pares.reverse() # Invierte el orden de los valores
    print(f"Los numeros pares son: {pares}")
    
main()