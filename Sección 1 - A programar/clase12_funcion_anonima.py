#Función normal
def cuadrado(x):
    return x ** 2
 
#Función anonima - Lambda (lambda parámetros: expresión)
cuad = lambda x: x ** 2

print(cuadrado(2))
print(cuad(2))

lista = [31, 28, 10, 15, 18, 22, 51, 13, 66, 77]

#Función map - sintaxis: map(function, iterables) - (nota: La función debe tener un parametro por cada iterable)
# https://www.w3schools.com/python/ref_func_map.asp
print(list(map((lambda valor: valor*valor), lista)))

#Función filter - sintaxis: filter(function, iterable)
# https://www.w3schools.com/python/ref_func_filter.asp
print(list(filter((lambda valor: valor%2==0),lista)))

#Función reduce - sintaxis: reduce(function, sequence[, initial]) -> value
# https://thepythonguru.com/python-builtin-functions/reduce/
import functools 
print(str(functools.reduce((lambda x,resultado: x+resultado),lista)))

#https://j2logo.com/python/funciones-lambda-en-python/