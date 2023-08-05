import os
def opcion_invalida():
    print("\nERROR: Ingrese una opción disponible\n")
    clean()

def clean():
    input("Presione una tecla para continuar...")
    os.system("cls") # Limpiar terminal