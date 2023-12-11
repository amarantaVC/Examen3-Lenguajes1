"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN2 - PREGUNTA 2
AMARANTA VILLEGAS 16-11247
Archivo testPregunta4.py, en este archivo se encuentran las pruebas unitarias para el archivo pregunta4.py
"""

from unittest import TestCase
from pregunta4 import *

class TestPregunta4(TestCase):

    def test_main(self):

        self.assertEqual(main("CLASS A f g"), "La clase A se definió con los metodos -> {'f': 'A', 'g': 'A'}")

        self.assertEqual(main("DESCRIBIR A"), "f -> A :: f\ng -> A :: g")

        self.assertEqual(main("CLASS A f g"), "Error: A ya existe")

        self.assertEqual(main("salir"), "Error: accion invalida")

        self.assertEqual(main("DESCRIBIR X"), "Error: X no existe")

        self.assertEqual(main("CLASS B : A f h"), "La clase B se definió con los metodos -> {'f': 'B', 'g': 'A', 'h': 'B'}")

        self.assertEqual(main("CLASS D m a m i"), "Error: los metodos deben tener nombres diferentes")

        self.assertEqual(main("CLASS C : M f h"), "Error: M no existe")
