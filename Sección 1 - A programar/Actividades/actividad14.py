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
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        self.entrada = self.hora_actual()
        self.tiempo = timedelta(hours=8) # Horas laborales
        self.salida = self.hora_salida()
        
    def hora_actual(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return datetime.now()
    
    def hora_salida(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.entrada+self.tiempo
     
    def horas_faltantes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        #return timedelta(hours=0) # Ver funcionamiento en comprobar_tiempo()
        return self.hora_salida()-self.hora_actual()
    
    def formato_datetime(self,fecha_hora):
        """_summary_

        Args:
            fecha_hora (_type_): _description_

        Returns:
            _type_: _description_
        """
        return fecha_hora.strftime("%H:%M:%S %d/%m/%Y")
        
    def comprobar_tiempo(self):
        """_summary_
        """
        if self.horas_faltantes()<=timedelta(hours=0): # hours = 0 - jornada concluida
            print(f"Su horario laboral ha concluido - Hora actual: {self.formato_datetime(self.hora_actual())} - Hora de salida: {self.formato_datetime(self.salida)}")
        else:
            print(f"Faltan {self.horas_faltantes()} para concluir su jornada laboral")
            
    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"Entrada: {(self.formato_datetime(self.entrada))} - Salida estimada: {self.formato_datetime(self.salida)} - Hora actual: {self.formato_datetime(self.hora_actual())}"

def main():
    """_summary_
    """
    trabajador01 = JornadaLaboral()
    trabajador01.comprobar_tiempo()
    print(trabajador01)
    
main()