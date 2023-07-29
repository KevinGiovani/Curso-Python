# - clave: Unica
# - valor: Cada clave tendra ascociado un valor, este puede ser un
# elemento, lista u otros
# pares (clave: valor)

diccionario = {'nombre':'Jose',
               'apellidos': 'Olmeda',
               'tutoriales': [
                   'Python',
                   'Javascript',
                   'PHP'
               ]}

print(diccionario)
print(type(diccionario)) # <class 'dict'>

print(diccionario['nombre']) # Jose
print(diccionario['tutoriales']) # ['Python', 'Javascript', 'PHP']
print(diccionario['tutoriales'][1]) # 'Javascript'

for clave in diccionario:
    print(clave,":",diccionario[clave])
    
# Metodos para los diccionarios

# Convertir a diccionario
persona = dict(nombre="Andres", apellidos="Vazquez", edad=48)
print(persona)
print(type(persona))

diccionario02 = dict(zip('aeiou',[1,2,3,4,5])) # Asigna la cadena a los valores por medio de zip()
print(diccionario02) # {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(type(diccionario02))

# El método items() devolverá cada elemento en un diccionario, 
# como tuplas en una lista.
print(diccionario02.items()) # dict_items([('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5)])

print(diccionario02.keys()) # dict_keys(['a', 'e', 'i', 'o', 'u'])
print(diccionario02.values()) # dict_values([1, 2, 3, 4, 5])

#diccionario02.clear()
#print(diccionario02) # {}

copia_diccionario = diccionario02.copy()
print(copia_diccionario)

diccionario03 = dict.fromkeys(['a','e', 'i', 'o','u'],34)
print(diccionario03) # {'a': 34, 'e': 34, 'i': 34, 'o': 34, 'u': 34}

print(diccionario.get('nombre')) # Jose
print(diccionario.get('tipo')) # None

borrado = diccionario.pop('nombre')
print(borrado) # Jose
print(diccionario) # {'apellidos': 'Olmeda', 'tutoriales': ['Python', 'Javascript', 'PHP']} 

# borrado2 = diccionario.pop('dirección') # KeyError: 'dirección'
# print(borrado2)

diccionario02 = {'provincia': "Sevilla",
                 'apellidos': 'Gutierrez'
                 }
print(diccionario)  # {'apellidos': 'Olmeda', 'tutoriales': ['Python', 'Javascript', 'PHP']}
diccionario.update(diccionario02)
print(diccionario) # {'apellidos': 'Gutierrez', 'tutoriales': ['Python', 'Javascript', 'PHP'], 'provincia': 'Sevilla'}