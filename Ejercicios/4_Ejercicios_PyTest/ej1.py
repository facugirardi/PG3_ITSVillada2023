"""Ejercicio 1: Validación de contraseña Escribe una función validate_password(password)  que tome una cadena como argumento y 
determine si cumple con los siguientes criterios de validez:

Tiene al menos 8 caracteres.
Contiene al menos una letra mayúscula, una letra minúscula y un número.
No contiene caracteres especiales. 
"""
import re


class Password:
    def validate_password(password):
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if re.search(r"\W", password):
            return False
        return True


class TestPassword():
    def test_validate_password_valid(self):
        assert Password.validate_password("Abcdefg1") == True
        assert Password.validate_password("Abc1") == False
        assert Password.validate_password("abcdefg1") == False
        assert Password.validate_password("Abcdefgh") == False
        assert Password.validate_password("Abcdefg1!") == False
