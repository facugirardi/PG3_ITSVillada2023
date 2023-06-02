"""Ejercicio 2: Conversión de números romanos Escribe una función roman_to_decimal(roman_number) que tome una
 cadena que representa un número romano y la convierta a su equivalente decimal.
"""

def roman_to_decimal(roman_number):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_number = 0

    for char in roman_number:
        decimal_number += roman_dict[char]

    return print(decimal_number)

roman_to_decimal('XIV')