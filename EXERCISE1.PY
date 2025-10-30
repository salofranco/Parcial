class persona:
    def __init__(self, nombre, apellido, edad, fechaNac):
        self.nombre = nombre      
        self.apellido = apellido  
        self.edad = edad  
        self.fechanac = fechaNac

class jugador(persona):
    def __init__(self, nombre, apellido, edad, numFed, fechaNac):
        super().__init__(nombre, apellido, edad, fechaNac)  
        self.numFed = numFed                      

jugador1 = jugador("Salome", "Franco", 20, 1234, "18/03/2008")

print("Nombre:", jugador1.nombre)
print("Apellido:", jugador1.apellido)
print("Edad:", jugador1.edad)
print("Número de Federación:", jugador1.numFed)
print("Fecha de Nacimiento:", jugador1.fechanac)

