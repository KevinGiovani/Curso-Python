#Obtener valores en python

nombre = input("Dime tu nombre: ")

#Formas de realizar el print en cadena
print("Hola "+nombre)
print("Hola",nombre) #Se agrega el espacio correspondiente
print(f"Hola {nombre}")

num1 = int(input("\nDime un numero: ")) # int - cambiar entrada a entero
num2 = int(input("Dime un segundo numero: "))

resultado = num1+num2

print("La suma de "+str(num1)+"+"+str(num2)+" tiene como resultado "+str(resultado))
print(f"La suma de {num1}+{num2} tiene como resultado {resultado}")

#Comunmente finaliza con salto de linea por defecto cada print 
print("Texto #1 finaliza con espacio",end=" ") #end - Cambio de salto de linea por espacio
print("Texto #2 finaliza con porcentaje ",end="% ") #Cambio de salto de linea por %

print("Texto #3 finaliza con tres saltos de linea \n\n\n")
print("Texto #4 \t\t esta separado por 2 tabulaciones")

print("Fecha",end=" ")
#Comunmente se colocan espacios por defecto como separador entre cada argumento 
print('30','06','2023', sep="/") #sep - Cambio de espacio por /