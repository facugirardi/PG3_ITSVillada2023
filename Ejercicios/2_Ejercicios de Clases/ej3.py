class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def imprimir_lado_mayor(self):
        print(max(self.lado_a, self.lado_b, self.lado_c))

    def imprimir_equilatero(self):
        if self.lado_a == self.lado_b and self.lado_a == self.lado_c:
            print("Es equilátero")
        else:
            print("No es equilátero")

triangulo1 = Triangulo(10, 10, 10)
triangulo1.imprimir_lado_mayor()
triangulo1.imprimir_equilatero()

triangulo2 = Triangulo(2, 4, 8)
triangulo2.imprimir_lado_mayor()
triangulo2.imprimir_equilatero()