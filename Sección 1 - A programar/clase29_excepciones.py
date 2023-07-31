import os

num1 = 50
num2 = 0
num3 = 10

# Ejemplo 1: Entre en la excepción
err = False
try:
    resultado = num1 / num2
    print(resultado, end="")
except ZeroDivisionError: 
    print("No se permite la división entre cero",end="")
    err = True
finally: # Ejecuta el codigo pase lo que pase
    if(err):
        print(" - Ocurrio un error")
    else:
        print(" - División realizada con exito")
        
# Ejemplo 2: No entra en excepción
err = False
try:
    resultado = num1 / num3
    print(resultado, end="")
except ZeroDivisionError: 
    print("No se permite la división entre cero",end="")
    err = True
finally:
    if(err):
        print(" - Ocurrio un error")
    else:
        print(" - División realizada con exito")
        
# Ejemplo 3: Eliminar un archivo que no existe
try:
    os.remove(os.getcwd() + "/archivo444.txt")
except FileNotFoundError as e:
    print(str(e)) # "[WinError 2] El sistema no puede encontrar el archivo especificado: ...."
finally:
    print(" ( Fin del proceso ) ".center(50,"*"))