texto = "Esto es un texto para el ejemplo que vamos a realizar"
#string.startswith()/string.endswith() - Compara si el valor especificado 
# coincide con el inicio/final del string utilizada
print("La cadena empieza con: ", texto.startswith("Esto")) # True
print("La cadena empieza con: ", texto.startswith("No")) # False

print("La cadena termina con: ", texto.endswith("realizar")) # True
print("La cadena termina con: ", texto.endswith("Realizando")) # False

print("La cadena empieza con: ", texto.upper().startswith("eSTo".upper())) 
print("La cadena termina con: ", texto.lower().endswith("REALizaR".lower()))

# Alinear texto (center(), ljust(), rjust())
# string.center(length, character): Alinea al centro el string
print(texto.center(80,'/'))

longitud_cadena = len(texto) # Tamaño del string - (53 characters)
print(longitud_cadena)
print(texto.center(longitud_cadena+7, '*')) #length=60

# string.ljust(length, character): Alinea a la izquierda el string
print(texto.ljust(80,'-'))

# string.rjust(length, character): Alinea a la derecha
print(texto.rjust(80,'+'))

# strip(): Eliminar espacios de inicio/final en blanco de string  
texto = "       Esto es una cadena con espacios y algunos caracteres speciales $!&=:;[].\=        "
print(texto)
print("Cadena sin espacios:", end=" ")
print(texto.strip())

# replace(old_value, new_value) : Sustituye lo especificado en el old_string
print(texto.replace("=:","hola"))