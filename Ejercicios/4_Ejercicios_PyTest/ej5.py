'''Ejercicio 5: Búsqueda en una matriz ordenada Escribe una función search_matrix(matrix, target) 
que tome una matriz ordenada de forma ascendente por filas y un número objetivo, y determine si el número está presente en la matriz.
'''

class Matriz:
    
    def search_matrix(matrix, target):
        if not matrix:
            return False

        filas = len(matrix)
        columnas = len(matrix[0])

        fila = 0
        columna = columnas - 1

        while fila < filas and columna >= 0:
            if matrix[fila][columna] == target:
                return True
            elif matrix[fila][columna] > target:
                columna -= 1
            else:
                fila += 1

        return False
    

class TestMatrix:
    matriz = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]]


    def test_matriz(self):
        assert Matriz.search_matrix(self.matriz, 5) == True
        assert Matriz.search_matrix(self.matriz, 10) == False
        assert Matriz.search_matrix([], 1) == False

