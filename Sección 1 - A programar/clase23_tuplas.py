# Las tuplas son parecidas a las listas pero con diferencia de que
# no se pueden modificar una vez creada (Inmutables)

colores = ("verde", "azul", "rojo", "morado", "gris") #No es necesario usar parentesis para que funcione
print(type(colores)) # <class 'tuple'>
print(colores)
print(colores[:2]) # ('verde', 'azul')

tupla = ()
print(type(tupla))
print(tupla)

# print(colores[6]) - IndexError: tuple index out of range
# colores[2] = "rosa" - TypeError: 'tuple' object does not support item assignment

print(len(colores)) # 5

# tupla_unitaria = (50) 
# print(type(tupla_unitaria)) - <class 'int'>
# print(len(tupla_unitaria)) - TypeError: object of type 'int' has no len()

tupla_unitaria = (50, )
print(type(tupla_unitaria)) # <class 'tuple'>
print(tupla_unitaria)
print(len(tupla_unitaria))

# Empaquetado de tuplas
a = 10
b = 'Jose'
c = 22.45
tupla = (a, b, c)
print(tupla)
print(type(tupla))

# Desempaquetado de tuplas
d, e, f = tupla
print(d)
print(e)
print(f)