"""
Funcion, area triangulo
Crea una funcion que calcule el area de un triangulo, recibiendo como parametros la base y la altura.
"""

__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

def ingresar_valores():
    """
    Entrada de datos de la figura por parte del usuario a 
    traves de la terminal

    Returns:
        list: base y altura
    """
    base = float(input("Ingrese el valor de la base (cm):"))
    altura = float(input("Ingrese el valor de la altura (cm): "))
    return [base, altura]

def calcular_area(base, altura):
    """
    Calculo del area del triangulo a partir de la formula (base*altura)/2
    
    Args:
        base (float): Valor de la base
        altura (float): Valor de la altura
        
    Returns:
        float: Valor del area
    """
    return (base*altura)/2

def main():
    """
    Llamado de las funciones de ingreso de valores y calculo del area
    para finalmente ser mostrada esta ultima en la terminal
    """
    print("Area del triangulo")
    base, altura = ingresar_valores()
    area = calcular_area(base, altura)
    print(f"El area del triangulo es de {area} cm^2" )
    
main()