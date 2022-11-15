""" import unittest
from luokka_kiekon_sijotus import KiekonSijoitus

SARAKKEET = 7

class TestKiekonSijotus(unittest.TestCase):
    def setUp(self):
        self.pelilauta = [0,0,0,0]
        #self.kiekon_sijotus = KiekonSijoitus.kiekon_sijoittaminen()

    def test_sijotus(self):
        KiekonSijoitus.kiekon_sijoittaminen(self.pelilauta)
        self.assertEqual(KiekonSijoitus.self.kiekko_lista, [1,0,0,0]) """