import unittest
from main import calcular_campeon

class TestCase3(unittest.TestCase):
    def test_calculo_campeon(self):
        resultados = [[3, 3, 2, 1], [3, 3, 2, 1]]
        sistemas_puntuacion = [[4, 3, 2, 1], [4, 3, 2, 1]]
        resultados_esperados = [[3, 4], [3, 4]]
        
        for resultado, sistema_puntuacion, resultado_esperado in zip(resultados, sistemas_puntuacion, resultados_esperados):
            mensaje_error = f"Error en el caso de prueba: {resultado}, {sistema_puntuacion}"
            self.assertEqual(calcular_campeon([resultado], sistema_puntuacion), resultado_esperado, mensaje_error)

if __name__ == '__main__':
    unittest.main()

