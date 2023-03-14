ancho = int(input("Ingrese ancho: "))
alto = int(input("Ingrese alto: "))
caracter = input("Ingrese caracter: ")

def dibujar_triangulo(ancho, caracter):
    for i in range(1, ancho+1):
        for j in range(i):
            print(caracter, end="")
        print()

    for i in range(1, ancho):
        for j in range(ancho - i):
            print(caracter, end="")
        print()


dibujar_triangulo(ancho, caracter)