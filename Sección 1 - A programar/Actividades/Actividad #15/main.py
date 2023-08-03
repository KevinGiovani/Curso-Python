"""
Modulo propio
Crea un modulo con las operaciones basicas de una calculadora.Importar el modulo
desde otro archivo python y llamar a las funciones creadas anteriormente, mostrando
su resultado por la consola.
"""

import calculadora

def control_errores(num1,num2):
    """
    Manejo de errores que pueden presentarse, en este caso solo se esta considerando 
    el error de la división entre cero
    
    Args:
        num1 (int/float)
        num2 (int/float)

    Returns:
        int/float: Resultado de la operación
    """
    try: #División
        return calculadora.division(num1,num2)
    except ZeroDivisionError:
        return "No se permite dividir entre cero"

print(calculadora.suma(20,8))
print(calculadora.resta(5, 10))
print(calculadora.multiplicacion(6, 6))
print(control_errores(20,5))
print(control_errores(20,0))