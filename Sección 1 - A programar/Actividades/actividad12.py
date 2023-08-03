"""
Clase vehiculo
Crea una clase Vehiculo con los siguientes atributos: Marca Color Crea la clase
Coche que herede de vehiculo y tenga los siguientes atributos: Potencia Motor 
Crear un objeto de clase Coche y mostrar sus atributos.
"""

__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

class Vehiculo():
    """
    Representa datos basicos sobre a un vehiculo general
    """
    def __init__(self, marca, color):
        """
        Inicialización de Vehiculo con argumentos de marca y color

        Args:
            marca (str): Fabricante que produjo el vehiculo
            color (str): Pintura de la carroceria
        """
        self.marca = marca
        self.color = color
        
    def __str__(self):
        """
        Información en formato legible en una cadena con los atributos del vehiculo

        Returns:
            str: Información descriptiva del vehiculo
        """
        return f"Marca: {self.marca}\nColor: {self.color}"
    
class Coche(Vehiculo):
    """
    Clase que hereda información de Vehiculo y esta además
    representa datos especificos de algun coche
    
    Args:
        Vehiculo (__main__.Vehiculo):  Clase de la que se hereda información sobre la marca y color
    """
    def __init__(self, marca, color, potencia, motor):
        """
        Inicialización de Coche y clase padre (Vehiculo)
        Args:
            marca (str): Fabricante
            color (str): Pintura
            potencia (str): Rapidez con la que puede trabajar el motor
            motor (str): Información relevante del motor
        """
        super().__init__(marca, color)
        self.potencia = potencia
        self.motor = motor
    
    def __str__(self):
        """
        Concatena los atributos de vehiculo mas los proporcionados en Coche 
        Returns:
            str : Información general sobre el coche
        """
        return Vehiculo.__str__(self)+f"\nPotencia: {self.potencia}\nMotor: {self.motor}"

def main():
    """
    Crea el objeto coche y vehiculo e imprime sus datos del objeto en la terminal
    """
    vehiculo = Vehiculo("Seat", "Morado")
    print(vehiculo, end="\n\n")
    coche = Coche("Ford","Rojo","350 HP","Motor 7.3L V8")
    print(coche)

main()