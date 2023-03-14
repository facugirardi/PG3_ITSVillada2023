def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end='')
        print()


ancho = int(input("Ingrese ancho: "))
alto = int(input("Ingrese alto: "))
caracter = input("Ingrese caracter: ")

dibujar_rectangulo(ancho, alto, caracter)

def dibujar_triangulo(ancho, caracter):
    for i in range(1, ancho+1):
        for j in range(i):
            print(caracter, end="")
        print()

    for i in range(1, ancho):
        for j in range(ancho - i):
            print(caracter, end="")
        print()

print('---------------------------------------')

dibujar_triangulo(ancho, caracter)