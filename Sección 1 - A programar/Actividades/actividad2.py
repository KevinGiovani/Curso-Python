"""
Ejercicio 02. Variable
Desde la consola Python, almacena el nombre del usuario en una variable 
y muestra por pantalla "Hola, [nombre]".
"""

__author__  = "Kevin G. Inzunza R."
__version__ = "1.0.0"

def main():
    """
    Saludo sencillo a usuario a partir del nombre dado
    en la entrada
    """
    name = input("Ingrese su nombre: ")
    print(f"Hola {name}")
    
main()