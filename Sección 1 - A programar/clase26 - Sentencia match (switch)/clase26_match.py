# Actividad realizada en la clase 25 pero en vez de la utilización
# de diccionarios se plantea el uso de la función match

def dame_meses(mes):
    match mes:
        case 1:
            print("Se ingreso enero")
        case 2:
            print("Se ingreso febrero")
        case 3:
            print("Se ingreso marzo")
        case 4:
            print("Se ingreso abril")
        case 5:
            print("Se ingreso mayo")
        case 6:
            print("Se ingreso junio")
        case 7:
            print("Se ingreso julio")
        case 8:
            print("Se ingreso agosto")
        case 9:
            print("Se ingreso septiembre")
        case 10:
            print("Se ingreso octubre")
        case 11:
            print("Se ingreso noviembre")
        case 12:
            print("Se ingreso diciembre")
        case _:
            print("No se ingreso un valor de mes valido")
        
mes = int(input("Introduce un numero correspondiente a algun mes (1 al 12): "))
dame_meses(mes)