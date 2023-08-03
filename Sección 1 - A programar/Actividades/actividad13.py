"""
Clase alumno
Crea una clase Alumno con su nombre y calificacion. Ademas de iniciar 
sus atributos, debes crear los metodos para mostrarlos e indicar si 
esta aprobado o no.
"""
__author__ = "Kevin G. Inzunza R"
__version__ = "1.0.0"

class Alumno():
    """
    Representa información basica sobre un alumno dentro de una materia
    escolar
    """
    def __init__(self, nombre, calificacion):
        """
        Inicialización de los atributos del Alumno
        Args:
            nombre (str)
            calificacion (int)
        """
        self.nombre = nombre
        self.calificacion = calificacion
        
    def aprobado(self):
        """
        Returns:
            str: Estado en la asignatura
        """
        return "Aprobado "if self.calificacion > 5 else "Reprobado"
    
    def __str__(self):
        """
        Cadena con datos sobre el estado (aprobado/reprobado) del alumno con sus respectivos datos de este

        Returns:
            str: Información sobre el nombre, promedio y estado
        """
        return f"Nombre: {self.nombre} - Calificación: {self.calificacion} | {self.aprobado()}"

def main():
    """
    Inicializa dos objetos de Alumno y en los cuales posteriormente
    se muestran en la terminal dado los datos que se ingreso
    """
    alumno1 = Alumno("Kevin", 8)
    alumno2 = Alumno("Joel", 5)
    print(alumno1)
    print(alumno2)
    
main()