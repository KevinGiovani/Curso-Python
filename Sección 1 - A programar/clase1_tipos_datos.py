#Tipos de variables
# str(value) - Concatenar con un formato cadena

num,dec,cadena,booleano=type(31),type(31.42),type('Hola'),type(True) #Declaración de variables

print('Tipos de datos')
print('Tipo entero: - '+ str(num))
print('Tipo decimal: - '+ str(dec))
print('Tipo cadena: - '+ str(cadena))
print('Tipo booleano: - '+ str(booleano)+'\n')

#Pruebas

print('Texto'+' en ' +'cadena')
print('Repetir '*3) #La multiplicación repetira las veces correspondientes la cadena

variable='cadena de variable'
variable='\nSumo esto a '+variable
variable2='CADENA NUMERO #2'

print(variable)
print(variable[3])
print(variable[-1]) 
print(variable[1:5]) #Muestra a partir del intervalo los caracteres
print(len(variable)) #Tamaño de la cadena
print(variable.upper()) #Visualización en mayuscula
print(variable2.lower()) #Visualización en minuscula
print(variable2.capitalize()) #Visualización de primer caracter en mayuscula y los demas minuscula

cadena= '   ,  Esta ,,, cadena cuenta con muchos espacios y comas  ,,,r  '
print(cadena)
print(cadena.strip(" ,r")) #Elimina cualquier carácter inicial (espacios al principio) y final (espacios al final) 
print(cadena.strip())

#remplazar valor
cadena = "Hola esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("sin reemplazar","reemplazado")) #Reemplaza una frase con otra en especifico