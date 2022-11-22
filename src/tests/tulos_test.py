import numpy as np
import unittest
from luokka_tulos import Tulos


RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4
pelilauta = np.zeros((RIVIT, SARAKKEET+1))
print(np.flip(pelilauta, 0))

class TestTulos(unittest.TestCase):
    def test_tulos(self):
        pelilauta = np.zeros((RIVIT, SARAKKEET+1))
        kiekko = 1
        a = Tulos.tulos_(pelilauta, kiekko)
        self.assertEqual(a, 0)