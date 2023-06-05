"""Ejercicio 2: Conversión de números romanos Escribe una función roman_to_decimal(roman_number) que tome una
 cadena que representa un número romano y la convierta a su equivalente decimal.
"""


class Number:
    def roman_to_decimal(roman_number):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal_number = 0

        for i in range(len(roman_number)):
            if i > 0 and roman_dict[roman_number[i]] > roman_dict[roman_number[i-1]]:
                decimal_number += roman_dict[roman_number[i]] - 2 * roman_dict[roman_number[i-1]]
            else:
                decimal_number += roman_dict[roman_number[i]]
        
        return decimal_number


class TestNum:
    def test_roman_to_decimal(self):
        assert Number.roman_to_decimal('XXIV') == 24
        assert Number.roman_to_decimal('IX') == 9
        assert Number.roman_to_decimal('LXXV') == 75
        assert Number.roman_to_decimal('MCMXCIV') == 1994
        assert Number.roman_to_decimal('CXLVIII') == 148
        assert Number.roman_to_decimal('MMMCMXCIX') == 3999
