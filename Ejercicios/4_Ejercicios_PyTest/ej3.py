"""Ejercicio 3: Verificación de anagramas Escribe una función is_anagram(word1, word2) que
 tome dos palabras como argumentos y determine si son anagramas (es decir, tienen las mismas letras en un orden diferente). 
"""

class Palabra:

    def is_anagram(pal1, pal2):
        pal1 = pal1.replace(" ", "").lower()
        pal2 = pal2.replace(" ", "").lower()

        return sorted(pal1) == sorted(pal2)
    

class TestPal:
    def test_pal(self):
        assert Palabra.is_anagram('amor', 'roma') == True
        assert Palabra.is_anagram('jorge', 'juan') == False
