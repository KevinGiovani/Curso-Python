lista_colores = ['Rojo','Amarillo', 'Verde', 'Azul']
mi_color = input('Ingrese un color: ')

for color in lista_colores:
    print(f"Color visualizado:{color}")
    if(mi_color==color):
        print("\nColor encontrado\n")
        break
else: #Se muestra al final del ciclo for (sin llegar al break)
    print('\nColor en la lista no encontrado\n')

#Ejercicio 2
rango_largo= range(1,1000)
for numero in rango_largo:
    print(numero)
    if(numero==5):
        print(f"Numero encontrado con valor {numero}")
        break
        # continue
else:
    print('Numero no encontrado')