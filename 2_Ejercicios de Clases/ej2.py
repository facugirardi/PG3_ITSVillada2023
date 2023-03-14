class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def nota(self):
        if self.nota>=6:
            print("Aprobado")
        else:
            print("Desaprobado")
