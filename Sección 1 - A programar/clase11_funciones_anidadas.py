def calcular(num1, num2, operacion="sumar"):
    def sumar(num1, num2):
        return num1+num2
    def restar(num1, num2):
        return num1-num2
    def multiplicar(num1, num2):
        return num1*num2
    def dividir(num1, num2):
        return num1/num2
    
    if(operacion=="sumar"):
        print(f"{num1} + {num2} = {sumar(num1,num2)}")
    elif(operacion=="restar"):
        print(f"{num1} - {num2} = {restar(num1,num2)}")
    elif(operacion=="multiplicar"):
        print(f"{num1} x {num2} = {multiplicar(num1,num2)}")
    elif(operacion=="dividir"):
        print(f"{num1} / {num2} = {dividir(num1,num2)}")  
    
calcular(3,4) #Por defecto se establecio en la funcion que se sumaria
calcular(5,1,"restar")
calcular(10,10,"multiplicar")
calcular(10,2,"dividir")
calcular(4,1,"sumar")