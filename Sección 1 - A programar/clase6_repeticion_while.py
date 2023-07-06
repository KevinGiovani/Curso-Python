# Tabla de multiplicar
tabla= int(input("¿Que tabla quieres calcular? "))

print(f"\nTabla del {tabla}")
cont=1 #Contador
#repeticion
while(cont<=10):
    res = tabla * cont #Resultado
    print(f"{tabla} x {cont} = {res}")
    cont = cont+1 #Incrementa el contador
    
print("\nFin de la tabla\n")

cont=1
#Ejemplo #2 (break)
while(cont<=10):
    res = tabla * cont #Resultado
    print(f"{tabla} x {cont} = {res}")
    if cont==5:
        print("\nEl contador es igual a 5 de modo que saldremos del bucle")
        break
    cont+=1 #Incrementa el contador
    
print("\nFin de la tabla\n")

cont=0
#Ejemplo #3 (continue)
while(cont<10):
    cont+=1 #Incrementa el contador
    if cont==3:
        print("El contador es igual a 3 de modo que no multiplicaremos por 3")
        continue #Detiene la actual iteración y continua con la siguiente
    res = tabla * cont #Resultado
    print(f"{tabla} x {cont} = {res}")
print("\nFin de la tabla\n")