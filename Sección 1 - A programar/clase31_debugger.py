def dividir():
    num1 = int(input("Dime el primer numero: "))
    num2 = int(input("Dime el segundo numero: "))
    try:
        resultado = num1/num2
    except ZeroDivisionError as err:
        resultado = "Error: " +str(err)
    finally:
        return resultado

def dame_pares():
    pares = []
    for i in range(1,51):
        if i % 2 == 0:
            pares.append(i)
    return pares

def main():
    print(dame_pares())

if __name__ == "__main__": # https://www.youtube.com/watch?v=Fh3RfVKWVII
    #print(dividir())
    main()