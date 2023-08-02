"""
Condicional, mayor de edad
Crea un script de Python que pregunte al usuario la edad y muestre por pantalla 
si es mayor de edad o no.
"""

def ingresar_edad():
    """
    Ingreso de edad a traves de la terminal
    Returns:
        int: Edad del usuario
    """
    edad = int(input("Ingrese su edad: "))
    return edad

def main():
    """
    Muestra en la terminal si el usuario es mayor edad o no
    dada la condición (mayor de 18 años)
    """
    print("¿El usuario es mayor de edad?")
    edad = ingresar_edad()
    tipo = "mayor de edad" if edad >= 18 else "menor de edad"
    print(f"El usuario es {tipo} ({edad})")
    
main()