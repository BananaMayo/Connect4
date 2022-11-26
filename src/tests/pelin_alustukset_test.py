import unittest
import numpy as np
from pelin_alustukset import PelinAlustukset

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100

class TestPelinAlustukset(unittest.TestCase):
    def setup(self):
        pass
    def test_luo_pelilauta(self):
        pelilauta = [[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,]]
        peli = PelinAlustukset
        lauta = peli.luo_pelilauta()
        pel = np.zeros((RIVIT, SARAKKEET))
        tulostus = peli.pelilaudan_tulostus(pel)
        self.assertEqual(tulostus, None)