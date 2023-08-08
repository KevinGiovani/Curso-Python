import os
def opcion_invalida():
    """
    Muestra mensaje de error y llama la función clean()
    """
    print("\nERROR: Ingrese una opción disponible\n")
    clean()

def clean():
    """
    Limpia todo el contenido de la terminal despues de que
    el usuario lo permita
    """
    input("Presione una tecla para continuar...")
    os.system("cls") # Limpiar terminal