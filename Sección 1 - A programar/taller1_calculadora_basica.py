def operaciones(entrada,num1,num2):
    if entrada==1: #Suma
        return (num1+num2),"+"
    elif entrada==2: #Resta
        return (num1-num2),"-"
    elif entrada==3: #Multiplicación
        return (num1*num2), "x"
    elif entrada==4: #Division
        return (num1/num2), "/"

error= "\nEntrada invalida"
while True:
    print("Calculadora basica")
    print("1 - Sumar", "2 - Restar", "3 - Multiplicar", "4 - Dividir", "0 - Salir",sep="\n")
    try:
        entrada = int(input("Ingrese una opción: "))
        if entrada in range(1,5):
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = operaciones(entrada,num1,num2)
            print(f"\nEl resultado de {num1} {resultado[1]} {num2} = {resultado[0]}",end="\n\n")
        elif entrada==0:
            break
        else:
           print(error, end="\n\n")
    except ValueError:
        print(error, end="\n\n")
    except ZeroDivisionError:
        print("\nNo se permite la división entre 0", end="\n\n")