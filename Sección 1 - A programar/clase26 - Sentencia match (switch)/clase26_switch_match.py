# Uso de switch por medio de match

def colores(color):
    match color:
        case 'rojo':
            print('Se ingreso el color rojo')
        case 'verde':
            print('Se ingreso el color verde')
        case 'naranja':
            print('Se ingreso el color naranja')
        case 'gris':
            print('Se ingreso el color gris')
        case _: # default
            print('Color no disponible')
            
entrada = input("Ingrese un color: ").lower()
colores(entrada)