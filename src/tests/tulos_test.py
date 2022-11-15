import numpy as np
import unittest
from luokka_tulos import Tulos


RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4

class TestTulos(unittest.TestCase):
    def setUp(self):
        self.tulos = 0

    def test_tulos(self):
        pelilauta = np.zeros((RIVIT, SARAKKEET+1))
        kiekko = 1

        keski_alue = [int(i) for i in list(pelilauta[:,SARAKKEET//2])]
        laske_keski_alue = keski_alue.count(kiekko)
        self.tulos += laske_keski_alue * 3

        a = Tulos._tulos(self, pelilauta, kiekko)

        self.assertEqual(self.tulos, 0)