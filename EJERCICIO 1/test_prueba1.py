import unittest
from palindromo import es_palindromo

class TestPrueba1(unittest.TestCase):
    def test_palabra(self):
        resultado = es_palindromo("reconocer")
        self.assertTrue(resultado)
        print("El resultado de la prueba 'test_palabra' es:", resultado)

if __name__ == "__main__":
    unittest.main()

