"""
Ejercicio 03. Mas sobre variables
Crea 2 variables, una tipo texto y otra numerica. Muestra cada variable y su tipo por consola.
"""

__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

def main():
    """
    Dos tipos de variables de diferente tipo que sirven como ejemplo
    de funcionamiento y las cuales son mostradas sus valores en consola
    """
    text = "Prueba de variable tipo texto"
    num = 210
    print(f"Variable de tipo texto: {text}")
    print(f"Tipo de la variable texto: {type(text)} \n")
    print(f"Variable de tipo numero: {num}")
    print(f"Tipo de la variable texto: {type(num)} \n")
    
main()