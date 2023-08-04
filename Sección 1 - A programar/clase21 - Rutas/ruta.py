import os
import pandas as pd

#Directorio actual
directorio_actual = os.path.dirname(__file__)
print(directorio_actual)

# Directorio datos
directorio_datos = os.path.join(directorio_actual, "Datos") #Concatena sin importar la forma en como se concatena las rutas ya sea en Windows o Linux por ejemplo "/" o "\" 
print(directorio_datos)

# Comprobar si existe un directorio
print(f"Existe el directorio: {os.path.exists(directorio_datos)}")

# Comprobar si es un directorio
print(f"¿Corresponde a un directorio? {os.path.isdir(directorio_datos)}")

# Listar archivos de directorio Datos
listado = [os.path.join(directorio_datos, item)
           for item in os.listdir(directorio_datos)]
print(listado)

print(os.listdir(directorio_datos))

# Crear carpeta
try:
    carpeta_nueva = os.mkdir(os.path.join(directorio_actual, "Nueva-carpeta"))
except FileExistsError:
    print("La carpeta ya existe")
    
# Abrir fichero datos de la raiz de esta clase
fichero_exterior = os.path.join(directorio_actual,"datos.csv")
df_exterior = pd.read_csv(fichero_exterior)
print(f"\nMostramos fichero exterior:\n{df_exterior}")

# Abrir fichero datos que se encuentra dentro del directorio Datos de esta clase
fichero_interior = os.path.join(directorio_datos,"datos.csv")
df_interior = pd.read_csv(fichero_interior)
print(f"\nMostramos fichero exterior:\n{df_interior}")

# Abrir sin indicar ruta (Para que funcione se debe agregar como Workspace el directorio de esta clase)
try:
    fichero = "datos.csv"
    df = pd.read_csv(fichero)
    print(f"\nMostrar fichero sin indicar ruta (Estando en el workspace correspondiente):\n {df}")
except FileNotFoundError:
    print("\nVerifica que se tiene agregado este directorio de esta clase en el area de Workspace")