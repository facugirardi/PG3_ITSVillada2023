alumnos = ['Juan', 'Facu', 'Jorge', 'Fede']

print(alumnos)
elem = input('Que elemento deseas consultar?:\n>>> ')

def busqueda(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
        else:
            continue


print(busqueda(alumnos, elem))