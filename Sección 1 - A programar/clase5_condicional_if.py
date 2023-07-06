print('¿Qué numero es mayor?')
num1= int(input("Dime el numero #1: "))
num2= int(input("Dime el numero #2: "))

if (num1>num2):
    print(f"\nEl numero #1 es mayor ({num1}) que el numero #2 ({num2})")
elif (num1<num2):
    print(f"\nEl numero #2 es mayor ({num2}) que el numero #1 ({num1})")
else:
    print(f"\nLos dos numeros son iguales: {num1} y {num2}")

print("\nProceso #1 terminado")


#Segundo ejemplo
print("\nTarifas por rango de edad")
edad=int(input("Ingresa tu edad: "))

if(edad<5):
    precio=0
elif(edad>18 and edad<25):
    precio=40
elif(edad>=25):
    precio=60
else:
    precio=20

print(f"Tu tarifa para entrar es de ${precio}")