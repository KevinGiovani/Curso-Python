"""
Archivo de texto
Crea un archivo de python donde abras un archivo txt y escribas texto dentro del
archivo. Despues abrir el archivo mediante codigo y mostrar el texto que contiene.
"""

__author__ = "Kevin G. Inzunza R"
__version__ = "1.0.0"

import os

def leer(file):
    """_summary_

    Args:
        file (_io.TextIOWrapper): _description_
    """
    print("\nContenido del archivo: ")
    print("*"*(50))
    file.seek(0) # El apuntador se dirige al inicio del archivo
    print(file.read())
    print("*"*(50))

def escribir(file):
    print("Ingrese el texto con la información que tendra el archivo: ")
    while True:
        linea = input("")
        file.write(linea+"\n")
        entrada = input("\n¿Desea finalizar de escribir o realizar un salto de linea? Escriba salir para finalizar, cualquier otra tecla se tomara como un salto de linea): ")
        if entrada.upper()=="SALIR":
            break
        else:
            print("\nSalto de linea...\n")

def crear_archivo():
    filename = input("¿Qué nombre desea ponerle al archivo?")
    cont = buscar_archivo(filename) # Verificar si ya existe
    if cont!=0:
        filename=filename+f"({cont}).txt"
        print(f"El nombre del archivo ingresado ya existe por lo que se modifico su nombre: {filename}")
    else:
        filename=filename+".txt"
    return open(filename,"w+")

def mostrar_archivos_txt():
    ruta_directorio = os.getcwd()
    archivos_txt = [item for item in os.listdir(ruta_directorio) if item.endswith(".txt")] # https://stackoverflow.com/questions/56860443/one-line-for-loop-to-add-elements-to-a-list-in-python
    print("*"*(50))
    print("Archivos de texto en el directorio actual:")
    print('\n'.join(archivos_txt))
    print("*"*(50))

def buscar_archivo(filename):
    cont = 0
    if os.path.exists(filename+".txt"):
        while True:
            cont += 1
            if os.path.exists(filename+f"({cont}).txt")==False:
                break
    return cont

def abrir_archivo():
    while True:
        mostrar_archivos_txt()
        filename = input("Ingrese el nombre del archivo a abrir (sin .txt): ")
        if buscar_archivo(filename)!=0: # El nombre de archivo ingresado si existe
            break
        print("\nEl nombre del archivo no existe. Por favor, ingrese otro\n")
    return open(filename+".txt", "a+")

def main():
    entrada = input("¿Desea crear un archivo o utilizar uno ya existente (Nuevo/Existe): ")
    try:
        if(entrada.upper() == "NUEVO"):
            file = crear_archivo()
        else: # Opción escogida = Existe
            file = abrir_archivo()
        escribir(file)
        leer(file)
        file.close()
    except:
        print("Ha ocurrido un error")

main()