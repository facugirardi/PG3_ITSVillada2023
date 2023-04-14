def funcion():
    while True:
        try:
            meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

            opcion = int(input("Ingresa el numero de mes:\n>>> "))

            print(meses[opcion-1])

        except IndexError:
            print("Numero no valido")

        except ValueError:
            print("Ingresa un numero")


funcion()