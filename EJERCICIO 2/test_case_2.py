import unittest
from main import calcular_campeon

class TestCase2(unittest.TestCase):
    def test_calculo_campeon(self):
        resultados = [[3, 2, 1]]
        sistemas_puntuacion = [[3, 2, 1], [1, 2, 3], [2, 1, 3]]
        resultado_esperado = [3, 1, 1]  # Corregido
        self.assertEqual(calcular_campeon(resultados, sistemas_puntuacion[0])[0], resultado_esperado[0])
        self.assertEqual(calcular_campeon(resultados, sistemas_puntuacion[1])[0], resultado_esperado[1])
        self.assertEqual(calcular_campeon(resultados, sistemas_puntuacion[2])[0], resultado_esperado[2])

if __name__ == '__main__':
    unittest.main()


