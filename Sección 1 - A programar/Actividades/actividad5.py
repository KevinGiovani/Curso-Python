"""
Calculo, indice de masa corporal
Realiza un programa de Python que pida al usuario su estatura y peso, 
los almacene en variables y los muestre por pantalla. nota: la fórmula para 
el IMC es el peso en kilogramos dividido por la estatura en metros cuadrados
"""

__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

def calculo_imc(datos):
    """
    Calculo del indice de masa corporal siguiendo su respectiva
    formula

    Args:
        datos (list): Valores del peso y estatura

    Returns:
        float: Valor del calculo del IMC en formato de dos decimales
    """
    imc = datos[1]/(datos[0]**2)
    return float(format(imc, ".2f"))
    
def ingresar_datos():
    """
    Ingreso de los datos necesarios por parte del usuario para el calculo del IMC
    
    Returns:
        list : Datos de estatura y peso
    """
    estatura = float(input("Ingrese su estatura en metros:"))
    peso = float(input("Ingrese su peso en kilogramos: "))
    return [estatura, peso]

def main():
    """ 
    Llamado de funciones para el ingreso de datos y el calculo del IMC
    para posteriormente ser mostrado en la terminal
    """
    print("Calculo de indice de masa corporal (IMC)")
    datos = ingresar_datos()
    imc = calculo_imc(datos)
    print(f"Su indice de masa corporal es de {imc}")
    
main()