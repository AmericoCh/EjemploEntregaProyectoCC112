# definición clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crea una instancia de la clase Persona
persona1 = Persona("Pedro", 23)
persona1.saludar()

# Crear una subclase de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_salario(self):
        print(f"Mi salario es {self.salario}.")

# instancia de la clase Empleado
empleado1 = Empleado("Pedro", 23, 1000)
empleado1.saludar()
empleado1.mostrar_salario()
