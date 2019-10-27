import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.palavra = "JURA"
        self.verbo = "clinicar"

    def test_gerar_frase_com_palavra_alnum(self):
        self.palavra_alnum = self.palavra + "0"
        self.assertRaises(Exception, main.gerar_frase(self.palavra, self.verbo))

    def test_gerar_frase_com_palavra(self):
        frase_esperada = "clinicar a JURA"
        self.assertEqual(frase_esperada, main.gerar_frase(self.palavra, self.verbo))
