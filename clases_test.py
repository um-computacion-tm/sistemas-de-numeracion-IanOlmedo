import unittest
from clases import Fecha, Persona, Ordenador
class Test(unittest.TestCase):
    def test1(self):
        pass




if __name__ == '__main__':
    persona = Persona(nombre='Peter', apellido='Parker', nacimiento=Fecha(año=1999,mes=12,dia=31))
    print(persona)