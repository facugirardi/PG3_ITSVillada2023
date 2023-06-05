'''Ejercicio 4: Cálculo de la media y desviación estándar Escribe una función calculate_statistics(numbers)
 que tome una lista de números como argumento y calcule su media y desviación estándar. 
'''

import math

class Numero:
    def calcular(numeros):
        n = len(numeros)
        media = sum(numeros) / n

        suma_diferencias_cuadrado = sum((x - media) ** 2 for x in numeros)
        varianza = suma_diferencias_cuadrado / n
        desviacion_estandar = math.sqrt(varianza)

        return media, desviacion_estandar


class TestNum:
    def test_num(self):
        assert Numero.calcular([1, 2, 3, 4, 5]) == (3.0, 1.4142135623730951)
        assert Numero.calcular([10, 20, 30, 40, 50]) == (30.0, 14.142135623730951)
        assert Numero.calcular([2.5, 3.5, 4.5, 5.5, 6.5]) == (4.5, 1.4142135623730951)

