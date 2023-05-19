import pytest

from ej1 import Persona

class TestPersona:
    def prueba_obj(self):
        persona = Persona('facu')
        assert persona.nombre == 'facu'

    def test_prueba(self):
        assert 'hola' == 'hola'
