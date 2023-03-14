class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

persona1 = Persona('Jorge')
persona2 = Persona('Facu')

persona1.mostrar_nombre()
persona2.mostrar_nombre()