def cont_vocales(frase):
    vocales = 0
    for letra in frase:
        if letra in 'aeiou':
            vocales += 1
    return vocales


frase = input("Ingrese una frase:\n>>> ")
print(frase)
print(cont_vocales(frase))