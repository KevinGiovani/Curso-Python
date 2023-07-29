class Vehiculo:
    def __init__(self, color, velocidad_max, marca): #Metodo constructor (siempre agregar self ya que hace referencia a la misma clase)
        self.color = color
        self.velocidad_max = velocidad_max
        self.marca = marca
        self.velocidad = -1
        
    def arrancar(self):
        if self.velocidad == -1:
            print("Arranque correcto")
            self.velocidad = 0
        else:
            print("El vehiculo ya ha sido arrancado anteriormente")
        
    def acelerar(self):
        if self.velocidad == -1:
            print("El vehiculo aun no ha sido arrancado")
        elif self.velocidad < self.velocidad_max:
            self.velocidad = self.velocidad + 10
            print(f"Velocidad = {self.velocidad}")
        else:
            print(f"Velocidad maxima ya alcanzada ({self.velocidad_max})")
    
    def desacelerar(self):
        if self.velocidad == -1:
            print("El vehiculo aun no ha sido arrancado")
        elif self.velocidad > 0:
            self.velocidad = self.velocidad - 10
            print(f"Velocidad = {self.velocidad}")
        else:
            print("El vehiculo se encuentra detenido")
    
    def info_status(self):
        print(f"\nMarca: {self.marca}\nColor: {self.color}\nVelocidad actual: {self.velocidad}\nVelocidad maxima: {self.velocidad_max} \n ")

class Moto(Vehiculo): # Herencia de la clase Vehiculo
    def __init__(self, color, velocidad_max, marca, ruedas=2):
        Vehiculo.__init__(self, color, velocidad_max, marca) # LLamado del init de la clase padre
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, velocidad_max, marca, ruedas=4):
        Vehiculo.__init__(self, color, velocidad_max, marca) # LLamado del init de la clase padre
        self.ruedas = ruedas
        
    def info_status(self):
        print(f"\nMarca: {self.marca}\nColor: {self.color}\nCantidad de ruedas: {self.ruedas}\nVelocidad actual: {self.velocidad}\nVelocidad maxima: {self.velocidad_max} \n ")


mi_vehiculo1 = Coche('rojo', 120,'Covini C6W',6) # Instanciar un objeto
mi_vehiculo1.desacelerar() # El vehiculo no ha sido arrancado
mi_vehiculo1.arrancar() # Arranque correcto
mi_vehiculo1.arrancar() # El vehiculo ya ha sido arrancado anteriormente
mi_vehiculo1.acelerar() # Velocidad = 10
mi_vehiculo1.info_status() # Marca: Peugeot, Color: rojo, Velocidad actual: 10, Velocidad maxima: 120

mi_vehiculo2 = Coche('azul', 140,'Renault')
mi_vehiculo2.acelerar() # El vehiculo no ha sido arrancado
mi_vehiculo2.arrancar() # Arranque correcto
while True:
    mi_vehiculo2.acelerar()
    if mi_vehiculo2.velocidad == mi_vehiculo2.velocidad_max:
        mi_vehiculo2.acelerar() # Velocidad maxima ya alcanzada (140)
        break
while True:
    mi_vehiculo2.desacelerar()
    if mi_vehiculo2.velocidad == 0:
        mi_vehiculo2.desacelerar() # El vehiculo se encuentra detenido
        break
mi_vehiculo2.info_status()

mi_vehiculo3 = Moto('morado', 115,'Yamaha')
mi_vehiculo3.arrancar() 
mi_vehiculo3.acelerar()
mi_vehiculo3.acelerar() 
mi_vehiculo3.info_status()