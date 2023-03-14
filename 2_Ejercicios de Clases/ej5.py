class Persona:
    def __init__(self):
        self.nombre = input('Ingresa tu nombre: ')
        self.edad = input('Ingresa tu edad: ')

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input('Ingresa su sueldo: '))
    
    def pagar_impuesto(self):
        if self.sueldo > 3000:
            print('Debe pagar impuestos')
        else:
            print('No debe pagar impuestos')


persona = Persona()
persona.mostrar()

empleado = Empleado()
empleado.mostrar()
empleado.pagar_impuesto()