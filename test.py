import unittest

from vocales import contar_vocales


class TestContarVocales(unittest.TestCase):
    def test_vacio(self):
        resultado = contar_vocales('fff')
        self.assertEqual(resultado, {})

    def test_solo_a(self):
        resultado = contar_vocales('fabr')
        self.assertEqual(resultado, {'a': 1})

    def test_2_vocales(self):
        resultado = contar_vocales('fabri')
        self.assertEqual(resultado, {'a': 1, 'i': 1})

    def test_3_vocales(self):
        resultado = contar_vocales('teclado')
        self.assertEqual(resultado, {'e': 1, 'a': 1, 'o': 1})

    def test_4_vocales(self):
        resultado = contar_vocales('computacion')
        self.assertEqual(resultado, {'o': 2, 'u': 1,'a': 1, 'i': 1})

    def test_5_vocales(self):
        resultado = contar_vocales('murcielago')
        self.assertEqual(resultado, {'u': 1, 'i': 1, 'e': 1, 'a': 1, 'o': 1})

    def test_mayusculas(self):
        resultado = contar_vocales('rEposItoriO')
        self.assertEqual(resultado,{'e': 1, 'o': 3, 'i': 2})




unittest.main()

