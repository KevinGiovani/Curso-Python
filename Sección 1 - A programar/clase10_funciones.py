def esPar(numero):
    if numero%2 == 0:
        # print("El numero es par")
        return True
    else:
        # print("El numero es impar")
        return False

print("¿El numero es par o impar?")
numero=int(input("Ingresa un numero:"))

resultado=esPar(numero)

print("El numero es",end=" ")
if resultado:
    print("par")
else:
    print("impar")