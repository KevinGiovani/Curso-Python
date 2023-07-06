#Por convención las variables se escriben en minuscula
#Damos valor a variable
precio, cantidad = 225, 3

#Calcular total
total = precio*cantidad

print("El precio total es de: $" +str(total))

#Borrar variable
del precio 
#print(precio) - Terminal: NameError: name 'precio' is not defined 

#Asignamos otros valores
precio=25
cantidad=21
total = precio*cantidad
print("El precio total es de: $" +str(total))

#Por convención las constantes se escriben en mayuscula
PASSWORD = "012345"
print(PASSWORD)

#Asignar varios valores
a, b, c, d = 1, 4,"Hola", True

print(a)
print(b)
print(c)
print(d)

#Asignar mismo valor (Asignación multiple)
x = y = z = 66

print(x)
print(z)