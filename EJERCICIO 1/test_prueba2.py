import unittest
from palindromo import es_palindromo

class TestPrueba2(unittest.TestCase):
    def test_frase(self):
        resultado = es_palindromo("anita lava la tina")
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
