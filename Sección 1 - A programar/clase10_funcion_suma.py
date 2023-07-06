def suma(num1, num2):
    return num1+num2

print("Suma de dos numeros")
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

resultado=suma(num1,num2) #Llamado a la función

print(f"El resultado de la suma de {num1} + {num2} es {resultado}")