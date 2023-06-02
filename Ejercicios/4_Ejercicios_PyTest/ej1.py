"""Ejercicio 1: Validación de contraseña Escribe una función validate_password(password)  que tome una cadena como argumento y 
determine si cumple con los siguientes criterios de validez:

Tiene al menos 8 caracteres.
Contiene al menos una letra mayúscula, una letra minúscula y un número.
No contiene caracteres especiales. 
"""

import re

def validate_password(password):
    if len(password) < 8:
        return False

    if not re.search('[A-Z]', password) or not re.search('[a-z]', password) or not re.search('[0-9]', password):
        return False

    if re.search('[^a-zA-Z0-9]', password):
        return False

    return True

passwords = ["Abcdefg1", "abc123", "ABCDEF123", "password123!"]
for password in passwords:
    if validate_password(password):
        print(f"La contraseña '{password}' es válida.")
    else:
        print(f"La contraseña '{password}' no cumple con los criterios de validez.")
