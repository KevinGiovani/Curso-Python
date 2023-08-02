"""
Funcion bisiesto
Escribe una funcion que indique si un año es bisiesto o no
"""

__author__ = "Kevin G. Inzunza R"
__version__ = "1.0.0"


def es_bisiesto(anio_consulta):
    """
    Comprueba si el año ingresado corresponde a un año bisiesto

    Args:
        anio_consulta (int): Año a comprobar

    Returns:
        bool : Si es bisiesto el año o no
    """
    
    #Para determinar si un año es bisiesto, siga estos pasos:
    # 1. Si el año es uniformemente divisible por 4, vaya al paso 2. 
    # De lo contrario, vaya al paso 5.
    # 2. Si el año no es uniformemente divisible por 100, vaya al paso 4. 
    # De lo contrario, vaya al paso 3.
    # 3. Si el año es uniformemente divisible por 400, vaya al paso 4. 
    # De lo contrario, vaya al paso 5.
    # 4. El año es un año bisiesto (tiene 366 días).
    # 5. El año no es un año bisiesto (tiene 365 días).
    comprobar = [4,100,400]
    if anio_consulta%comprobar[0] == 0: # Si no entra en la condición no es bisiesto
        if(anio_consulta%comprobar[1]!=0 or anio_consulta%comprobar[2]==0):
            return True
    return False

def main():
    """
    Imprime en la terminal si el año que fue ingresado desde el apartado del codigo
    corresponde a un año bisiesto
    """
    anio = 2012
    print(f"¿El año {anio} es bisiesto? {es_bisiesto(anio)}")
    
main()