"""
¿Funcion es primo?
Escribe una funcion que devuelva un valor booleano indicando si el
numero es primo o no.
"""

def es_primo(numero):
    """
    Comprobación del numero ingresado corresponde o no a un numero primo
    
    Args:
        numero (int): valor que se consultara

    Returns:
        bool : Tipo de valor primo (True) o compuesto (False)
    """
    
    # Recorre el conjunto de numeros menores al valor en consulta dado que posteriores
    # a este todos tendran un residuo y ademas un numero primo es mayor a 1 (por eso 
    # el rango comienza en 2) y distinto a el mismo.
    for divisor in range(2,numero):
        if numero%divisor == 0: # Si el residuo es cero entra en la condición (no es primo)
            return False
    return True
    
def main():
    """
    A partir de un numero ingresado desde el apartado del codigo
    se consultara si dicho valor si es par o no y se mostrara
    su resultado en la terminal
    """
    num = 23
    print(f"¿El numero {num} es primo? {es_primo(num)}")
    
main()