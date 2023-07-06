# Tabla de multiplicar
tabla= int(input("¿Que tabla quieres calcular? "))

print(f"\nTabla del {tabla}")

#Repetir mientras sea menor a 11
for cont in range (1,11):
    res = tabla * cont #Resultado
    print(f"{tabla} x {cont} = {res}")
else:
    print("\nFin de la tabla\n")


#Ejemplo #2 (for con break)
for cont in range (1,11):
    res = tabla * cont #Resultado
    print(f"{tabla} x {cont} = {res}")
    if(cont==5):
        print("\nEl contador es igual a 5 de modo que saldremos del bucle\n")
        break
else: #Se muestra al final del ciclo for(sin llegar al break)
    print("\nFin de la tabla\n")

#Ejemplo #3 (for con lista)
nombres = ["Jose", "Maria", "Ricardo", "Pedro"]
for nombre in nombres:
    print(f"Hola {nombre}!")
    
#Ejemplo #4 (Mostrar 100 numeros)
for i in range(100):
    print(i+1)
