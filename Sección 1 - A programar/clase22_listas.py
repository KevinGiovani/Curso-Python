lista = [1, 2, 3, 'Jose', [7, 8], 12]

print(type(lista))
print(lista)

print(lista[2]) # 3
print(lista[3][2]) # "s"
print(lista[4][1]) # 8
print(lista[1:4]) # 2, 3, 'Jose'
print(lista[2:6:2]) # 3, [7, 8]

for elemento in lista:
    print(elemento)


# Agregar elementos a la lista
lista.append(10)
lista.append("Alicia")
print(lista) # [1, 2, 3, 'Jose', [7, 8], 12, 10, 'Alicia']

lista.append([17, 2]) # En este caso se agrega como un solo elemento en la lista
print(lista) # [1, 2, 3, 'Jose', [7, 8], 12, 10, 'Alicia', [17, 2]]
 
lista.extend([2, 'Rosa']) # En este segundo caso se agrega como elementos individuales
print(lista) # [1, 2, 3, 'Jose', [7, 8], 12, 10, 'Alicia', [17, 2], 2, 'Rosa']

# Eliminar elementos de la lista
# Remueve la primera ocurrencia dado el valor ingresado
lista.remove(2)
print(lista) # [1, 3, 'Jose', [7, 8], 12, 10, 'Alicia', [17, 2], 2, 'Rosa']

lista.remove('Jose')
print(lista) # [1, 3, [7, 8], 12, 10, 'Alicia', [17, 2], 2, 'Rosa']

# Mostrar la posición en que se encuentre dicho valor
print(lista.index('Alicia')) # 5

# Retorna las veces en que se repite el valor
# Nota: No cuenta los valores de una lista dentro de otra lista
print(lista.count(2)) # 1

lista.reverse() # Invierte el contenido de la lista
print(lista) # ['Rosa', 2, [17, 2], 'Alicia', 10, 12, [7, 8], 3, 1]

# Mas ejemplos
lista_compra = ['pan', 'patatas', 'naranjas', 'manzanas', 'toronjas']
print(lista_compra)
# Crear una lista desde variables
cantidad_pan = 5
precio_pan = 24
total = cantidad_pan*precio_pan
pedido01 = [cantidad_pan, precio_pan, total]
pedido02 = [3, 50, 3*50]
pedido03 = [6, 12, 6*12]
pedidos = [pedido01, pedido02, pedido03]
print(pedido01) # [5, 24, 120]
print(pedidos) # [[5, 24, 120], [3, 50, 150], [6, 12, 72]]

# Lista vacia
lista_vacia = []
print(lista_vacia) # []

print(lista_compra)
lista_compra.append("peras")
lista_compra.insert(2, "uvas") # Ingresa el valor en una posición especifica
print(lista_compra) # ['pan', 'patatas', 'uvas', 'naranjas', 'manzanas', 'toronjas', 'peras']

lista_compra.pop() #Eliminar el ultimo elemento
print(lista_compra) # ['pan', 'patatas', 'uvas', 'naranjas', 'manzanas', 'toronjas']

# Longitud de lista
print(len(lista_compra)) # 6

# Ejemplo añadir un bucle for
cuadrados = []
for numero in range(1,10):
    cuadrados.append(numero*numero)
print(cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(min(cuadrados))
print(max(cuadrados))
print(sum(cuadrados))

# Buscar si se encuentra el valor en la lista
print("manzanas" in lista_compra) # True
print("piña" in lista_compra) # False
