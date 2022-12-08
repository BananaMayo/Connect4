import numpy as np
import unittest
from luokka_tulos import Tulos


RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4


class TestTulos(unittest.TestCase):
    def setUp(self) -> None:
        self.pelilauta = np.zeros((RIVIT, SARAKKEET))

    def test_tulos(self):
        lauta = np.zeros((RIVIT, SARAKKEET))
        kiekko = 1
        a = Tulos.tulos_(lauta, kiekko)
        self.assertEqual(a, 0)

    def test_tulos_2(self):
        pelilauta = np.ones((RIVIT, SARAKKEET))
        kiekko = 1
        a = Tulos.tulos_(pelilauta, kiekko)
        self.assertEqual(a, 6918.0)