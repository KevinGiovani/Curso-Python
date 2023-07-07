cadena = "EJemPLo De CaDeNa De TeXTo"

print(cadena.lower()) #Retorna la cadena en minuscula

print(cadena.upper()) #Retorna la cadena en mayuscula

print(cadena.capitalize()) #Retorna el primer caracter de la cadena en mayuscula

print(cadena.title()) #Retorna el caracter inicial de cada palabra en mayuscula y las demas en minuscula sobre la cadena

print(cadena.swapcase()) #Retorna de forma invertida las mayusculas/minusculas presentes en la cadena

print(cadena.isupper()) #Compara si la cadena esta en mayuscula
mayus="MAYUSCULA"
print(mayus.isupper())

print(mayus.islower()) #Compara si la cadena esta en minuscula
minus="minuscula"
print(minus.islower()) 

print(minus.isnumeric()) #Compara si la cadena es numerica
num="213"
print(num.isnumeric())

print(num.isalnum()) #Compara si la cadena es alfanumerica
cadena="$%&/()"
print(cadena.isalnum())

titulo="Titulo 1"
print(titulo.istitle()) #Compara si la cadena esta utilizando el formato de la función title()
no_titulo="Esto no es un titulo"
print(no_titulo.istitle())
