import unittest
from main import calcular_campeon

class TestCase1(unittest.TestCase):
    def test_calculo_campeon(self):
        resultados = [[3, 2, 1]]
        sistema_puntuacion = [3, 2, 1]
        resultado_esperado = [3]
        self.assertEqual(calcular_campeon(resultados, sistema_puntuacion), resultado_esperado)

if __name__ == '__main__':
    unittest.main()

