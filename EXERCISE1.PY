class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")


class Jugador(Persona):
    def __init__(self, nombre, apellido, edad, numFed):
        super().__init__(nombre, apellido, edad)
        self.numFed = numFed

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Número de Federación: {self.numFed}")

def main():
    print("=== Registro de Jugador ===")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    numFed = int(input("Ingrese el número de federación: "))

    jugador1 = Jugador(nombre, apellido, edad, numFed)

    print("\n--- Datos del Jugador ---")
    jugador1.mostrar_datos()


if __name__ == "__main__":
    main()


