def function():
    try:
        with open('archivo.txt', 'w') as archivo:
            strings = ['Hola', 'como', 'estas']
            for s in strings:
                archivo.write(s + '\n')
            archivo.write(123)
    except TypeError:
        print('Error: no se puede escribir un entero en un archivo de texto')

function()