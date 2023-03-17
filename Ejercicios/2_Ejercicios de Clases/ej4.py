class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(self.suma())
        print(self.resta())
        print(self.multiplicacion())
        print(self.division())

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2
    
operacion = Operaciones(4, 2)   