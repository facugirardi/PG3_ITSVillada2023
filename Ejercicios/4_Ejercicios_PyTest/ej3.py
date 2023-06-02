"""Ejercicio 3: Verificación de anagramas Escribe una función is_anagram(word1, word2) que
 tome dos palabras como argumentos y determine si son anagramas (es decir, tienen las mismas letras en un orden diferente). 
"""

def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    return sorted(word1) == sorted(word2)

if is_anagram('llenaba','ballena'):
    print('Son anagramas')
else:
    print('No son anagramas')