"""
Lista
Pedir al usuario una lista de colores (separados por comas), guardarlos en una
lista. No se deben guardar colores repetidos. Mostrar por consola la lista de 
colores ordenados alfabeticamente.
"""

def lista_colores(colores):
    """
    Pasa el contenido de la cadena a una lista para ordenarla alfabeticamente
    sin elementos repetidos y mostrarla en la terminal

    Args:
        colores (str)
    """
    lista = colores.split(",") 
    lista = [item.strip() for item in lista] # Elimina los espacios en blanco al inicio y final del elemento
    lista = list(set(lista))      
    lista.sort() # Ordenar alfabeticamente
    print(lista,end="\n\n")
    
def main():
    colores = input("Ingrese sus colores separados por coma: ")
    print("\nLista de colores ordenados alfabeticamente sin repetir:")
    lista_colores(colores)
    
main()