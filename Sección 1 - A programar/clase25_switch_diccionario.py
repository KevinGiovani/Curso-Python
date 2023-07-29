# Uso de switch con diccionarios

# Ejemplo:Usuario nos da un numero de un mes y nosotros lo pasamos a su correspondiente valor
def dame_mes(num):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return meses.get(num, "Mes no valido")

#print(dame_mes(3)) # Marzo

mes = int(input("Introduce un numero correspondiente a algun mes (1 al 12): "))
print(dame_mes(mes))