"""Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, capturar la excepción ZeroDivisionError."""

try:
    n1 = int(input("Ingresa el primer numero:\n>>> "))
    n2 = int(input("Ingresa el segundo numero:\n>>> "))

    print(n1/n2)

except ZeroDivisionError:
    print("No se puede dividir por cero")
