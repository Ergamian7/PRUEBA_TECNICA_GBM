import unittest
from palindromo import es_palindromo

class TestPrueba3(unittest.TestCase):
    def test_frase_con_espacios(self):
        resultado = es_palindromo("a la gorda drogala")
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
