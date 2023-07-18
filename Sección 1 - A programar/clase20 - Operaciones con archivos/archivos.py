from msilib import CreateRecord
import os

# Obtiene el directorio de este archivo en uso y concatena con la 
# carpeta en cuestión a trabajar, esto con la intención de no depender
# del workspace activo (os.getcwd())
carpeta = os.path.dirname(__file__)+"\mi-carpeta"
#print(carpeta)
listado = os.listdir(carpeta)
print(listado)
print(type(listado))

# Filtrado
for archivo in listado:
    if archivo.endswith(".txt"):
        print("Fichero TXT encontrado: " +archivo)

#  Otra forma de filtrado
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://geekflare.com/es/filter-list-in-python/
filtrado = [archivo for archivo in listado if archivo.endswith(".pdf")]
print(filtrado)

os.chdir(carpeta)
#print(os.getcwd())

# Renombrar (Comentar alguna de las siguientes lineas segun corresponda
# para visualizar funcionalidad)
#os.rename("Archivo-Winrar4.rar", "renombrado.rar")
#os.rename("renombrado.rar", "Archivo-Winrar4.rar")

# Borrar nota: este archivo ya ha sido borrado, usar otro.
# os.remove("Archivo-ejemplo1.txt")

# Renombrar varios archivos a la vez
contador = 1
for archivo in os.listdir():
    nombre, extension = os.path.splitext(archivo)
    nuevo_nombre = str(contador)+"-"+nombre+extension
   # Descomentar siguiente linea para efectuar los cambios de nombre
   # os.rename(archivo, nuevo_nombre) 
    contador += 1
    
# Copiar contenido de un archivo a otro
try:
    fichero = open("test.txt","r")
    nuevo_fichero = open("nuevo-test.txt", "w")

    for linea in fichero:
        nuevo_fichero.write(linea)

    fichero.close()
    nuevo_fichero.close()
except FileNotFoundError:
    print("El archivo no ha sido encontrado / El archivo no existe")
    
# Otra forma de copiar un archivo a otro
# Usando este metodo (with) no es necesario especificar la linea de codigo de close() 
# del archivo abierto ya que automaticamente lo realiza el cerrado
try:
    with open('test.txt') as fichero: #Por defecto es lectura al no definirle el modo - (as) representa el alias
        with open("nuevo-test.txt", "w") as nuevo_fichero:
            for linea in fichero:
                nuevo_fichero.write(linea)
except FileNotFoundError:
    print("El archivo no ha sido encontrado / El archivo no existe")