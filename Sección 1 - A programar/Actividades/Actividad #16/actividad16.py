"""
Archivo de texto
Crea un archivo de python donde abras un archivo txt y escribas texto dentro del
archivo. Despues abrir el archivo mediante codigo y mostrar el texto que contiene.
"""

__author__ = "Kevin G. Inzunza R"
__version__ = "1.0.0"

import os

def leer(file):
    """
    Realiza la lectura de la información del archivo de forma completa
    y es presentada dentro de la terminal
    
    Args:
        file (_io.TextIOWrapper): Contenido de lectura
    """
    print("\nContenido del archivo: ")
    print("*"*(50))
    file.seek(0) # El apuntador se dirige al inicio del archivo
    print(file.read())
    print("*"*(50))

def escribir(file):
    """
    Escribe dentro del archivo el texto ingresado por el usuario
    
    Args:
        file (_io.TextIOWrapper): Archivo al que se le ingresara contenido de texto
    """
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
    """
    Creación del archivo a manipular. El nombre del archivo es proporcionado
    por el usuario desde la terminal, en caso de que ya exista uno con el mismo
    nombre dentro directorio con todos los archivos, este nuevo automaticamente
    se le agregara una extension a su nombre de tipo numerica para identificarlo.

    Returns:
        _io.TextIOWrapper : Archivo de texto en modo escritura y lectura
    """
    filename = input("¿Qué nombre desea ponerle al archivo?")
    cont = comprobar_archivo(filename)
    if cont!=0:
        filename=filename+f"({cont}).txt"
        print(f"El nombre del archivo ingresado ya existe por lo que se modifico su nombre: {filename}")
    else:
        filename=filename+".txt"
    return open(filename,"w+")

def mostrar_archivos_txt():
    """
    Muestra dentro de la terminal todos los archivos con extensión .txt que se encuentran en el directorio utilizado (directorio del proyecto)
    """
    ruta_directorio = os.getcwd()
    archivos_txt = [item for item in os.listdir(ruta_directorio) if item.endswith(".txt")] # https://stackoverflow.com/questions/56860443/one-line-for-loop-to-add-elements-to-a-list-in-python
    print("*"*(50))
    print("Archivos de texto en el directorio actual:")
    print('\n'.join(archivos_txt))
    print("*"*(50))

def comprobar_archivo(filename):
    """
    Realiza la busqueda del archivo a partir del nombre en el directorio actual 
    y en dado caso que exista algun problema aumenta el contador hasta que no se encuentre una igualdad en el nombre

    Args:
        filename (str)

    Returns:
        int: Contador de repeticiones de nombre del archivo
    """
    cont = 0
    if os.path.exists(filename+".txt"):
        while True:
            cont += 1
            if os.path.exists(filename+f"({cont}).txt")==False: # Nuevo posible nombre a asignar (filename(cont))
                break
    return cont

def abrir_archivo():
    """
    Abre un archivo disponible en el directorio dada la elección del usuario dentro de la terminal

    Returns:
        _io.TextIOWrapper : Archivo de texto en modo escritura y lectura manteniendo el contenido 
        de las modificaciones hechas anteriormente
    """
    while True:
        mostrar_archivos_txt()
        filename = input("Ingrese el nombre del archivo a abrir (sin .txt): ")
        if os.path.exists(filename+".txt"): # El nombre de archivo ingresado si existe
            break
        print("\nEl nombre del archivo no existe. Por favor, ingrese otro\n")
    return open(filename+".txt", "a+")

def main():
    """
    Permite que el usuario desde la terminal utilice un archivo de texto nuevo o existente
    en el cual podra ingresarle mas contenido y posteriormente lo visualizara
    """
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