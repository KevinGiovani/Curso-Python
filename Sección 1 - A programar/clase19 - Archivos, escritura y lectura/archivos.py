# Guardar datos en archivo
escritura = open("archivo.txt", "w") # Abrir archivo en modo de escritura

escritura.write("Esto se escribe en el archivo \n"
                +"Y esto en la linea siguiente"
                +"\n\t\t\tY esto en otra linea con inicio tabulado")

escritura.close()

# Lectura de fichero
lectura = open("archivo.txt","r") # Modo lectura

lee_linea = lectura.readline() # Lectura de una linea
print("Leyendo una linea:\n" +lee_linea)
lectura.close()

# Lectura completa
lectura = open("archivo.txt","r") # Modo lectura

lectura_completa = lectura.read()
print("Leyendo todo el archivo de texto:\n" +lectura_completa)
lectura.close()

lectura = open("archivo.txt","r") # Modo lectura
lectura_completa = lectura.readlines() # Devuelve una lista con cada linea
print("Contenido en lista:" +lectura_completa[1])
lectura.close()