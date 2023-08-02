"""
Ejercicio 04. Modifica variables
Modifica las variables del ejercicio anterior muestra el antes y 
el despues de cada variable por consola.
"""
__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

def main():
    """
    Dos tipos de variables de las cuales se les puede realizar un cambio
    de contenido posterior al primer uso (ANTES) y ver que siguen funcionando
    a pesar de que se modifica el tipo de esta.
    """
    text = "Prueba de variable tipo texto"
    num = 210
    print(f"ANTES:\nVariable de tipo texto: {text}")
    print(f"Tipo de la variable texto: {type(text)} \n")
    print(f"Variable de tipo numero: {num}")
    print(f"Tipo de la variable texto: {type(num)} \n")
    
    text = 250
    num = "Modificación de variable"
    print(f"DESPUES:\nVariable de nombre 'text': {text}")
    print(f"Tipo de la variable: {type(text)} \n")
    print(f"Variable de nombre 'num': {num}")
    print(f"Tipo de la variable: {type(num)} \n")
       
main()