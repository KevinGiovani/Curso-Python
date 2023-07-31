# Pagina con la que se genero los datos: https://www.mockaroo.com/
# Fields_name: id, nombre, apellidos, email, genero.
# Rows: 500, Format: JSON

import json
from urllib import request

url = "https://my.api.mockaroo.com/personas.json?key=7fbe9f90" # Route: GET /personas.json
respuesta = request.urlopen(url)
#print(respuesta.read())

contenido = respuesta.read()
#print(contenido)

json_obtenido = json.loads(contenido.decode('utf-8'))
#print(json_obtenido)

# Ejemplo 1
for persona in json_obtenido:
    print(persona, end="\n\n")

# Ejemplo 2
for persona in json_obtenido:
    print(f"Nombre: {persona['nombre']}", end="\n\n")
    
# Ejemplo 3
for persona in json_obtenido:
    print(" + - + ".center(40,"*"))
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido(s): {persona['apellidos']}")
    print(f"Email: {persona['email']}")
    print(" + - + ".center(40,"*"), end="\n\n")
