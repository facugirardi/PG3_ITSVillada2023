class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def nota_mostrar(self):
        if self.nota>=6:
            print("Aprobado")
        else:
            print("Desaprobado")

alumno1 = Alumno("Juan", 7)
alumno1.imprimir()
alumno1.nota_mostrar()

alumno2 = Alumno("Facu", 1)
alumno2.imprimir()
alumno2.nota_mostrar()