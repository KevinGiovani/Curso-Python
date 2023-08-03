"""
Modulo DateTime
Crear un script que indique si has terminado tu jornada laboral, por ejemplo que
compruebe si son las 19.30, en caso contrario indicar cuanto tiempo queda. Hacer
uso del modulo datetime, para comprobar la hora.
"""

__author__ = "Kevin G. Inzunza R."
__version__ = "1.0.0"

from datetime import datetime, timedelta

class JornadaLaboral():
    """
    Representación de una jornada laboral en la cual se debe cumplir un cierto
    tiempo en horas para establecer la salida de un empleado, y en dado caso
    de aun no cumplirlas mostrar el tiempo estimado para lograrlo
    """
    def __init__(self):
        """
        Inicializa las variables relevantes como la entrada, 
        tiempo que se debe cumplir en la jornada de trabajo y
        el tiempo exacto de cuando se debe dar la salida
        """
        self.entrada = self.datetime_actual()
        self.tiempo = timedelta(hours=8) # Horas laborales
        self.salida = self.entrada+self.tiempo
        
    def datetime_actual(self):
        """
        Obtiene información especifica del modulo datetime
        
        Returns:
            datetime.datetime : Fecha y hora actual
        """
        return datetime.now()
     
    def horas_faltantes(self):
        """
        Obtiene el tiempo necesario que falta para concluir la jornada
        a partir de la hora estimada de salida menos la hora actual
        en la cual se consulta
        
        Returns:
            datetime.timedelta: Tiempo faltante para concluir la jornada
        """
        #return timedelta(hours=0) # Ver funcionamiento en comprobar_tiempo()
        #return timedelta(hours=3, minutes=15)
        return self.salida-self.datetime_actual()
    
    def formato_datetime(self, fecha_hora, add_date = True):
        """
        Modificación de la fecha (dia,mes,año) y hora (hora,minuto,segundo) pasandolo a un formato general
        
        Args:
            fecha_hora (datetime.datetime): Información de la fecha y hora sin formato
            add_date (bool): Permite ingresar a la cadena el formato con fecha

        Returns:
            str: Cadena de información con formato de la fecha y hora o solo hora
        """
        if add_date:
            return fecha_hora.strftime("%H:%M:%S %d/%m/%Y")
        else:
            return fecha_hora.strftime("%H:%M:%S")
        
    def comprobar_tiempo(self):
        """
        Comprueba si se ha cumplido con las horas de una jornada, de ser asi
        muestra en la terminal que se ha concluido y ademas muestra el tiempo actual y cuando fue salida,
        en caso contrario de aun no cumplir con las horas necesarias, se muestra en la terminal
        el tiempo faltante para concluir la jornada.
        """
        if self.horas_faltantes()<=timedelta(hours=0): # hours = 0 - jornada concluida
            print(f"Su horario laboral ha concluido - Actual: {self.formato_datetime(self.datetime_actual())} - Salida: {self.formato_datetime(self.salida)}")
        else:
            print(f"Faltan {self.horas_faltantes()} para concluir su jornada laboral")
            
    def __str__(self):
        """
        Contenido concatenado con la información general sobre la jornada laboral

        Returns:
            str: Entrada, salida estimada y hora actual
        """
        return f"Entrada: {(self.formato_datetime(self.entrada))} - Salida estimada: {self.formato_datetime(self.salida)} - Hora actual: {self.formato_datetime(self.datetime_actual(), False)}"

def main():
    """
    Crea un objeto de la clase JornadaLaboral y hace el llamado de funciones
    correspondientes a esta para ser mostrada su información dentro de la terminal
    """
    trabajador01 = JornadaLaboral()
    trabajador01.comprobar_tiempo()
    print(trabajador01)
    
main()