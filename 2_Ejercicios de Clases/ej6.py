class Familia:
    def __init__(self, padre, madre, hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
        
    def __str__(self):
        return f"Padre: {self.padre}\nMadre: {self.madre}\nHijos: {self.hijos}"
    

hijos = ['Facundo', 'Valentino', 'Jorge', 'Juan']

familia = Familia('Jose', 'Sofia', hijos)
print(familia.__str__())
