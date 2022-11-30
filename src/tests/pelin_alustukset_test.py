import unittest
import numpy as np
from pelin_alustukset import PelinAlustukset

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100

class TestPelinAlustukset(unittest.TestCase):
    def setUp(self) -> None:
        self.peli = PelinAlustukset


    def test_luo_pelilauta(self):
        pelilauta = [[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,],[0., 0., 0., 0., 0., 0., 0.,]]
        lauta = self.peli.luo_pelilauta()
        pel = np.zeros((RIVIT, SARAKKEET))
        tulostus = self.peli.pelilaudan_tulostus(pel)
        self.assertEqual(tulostus, None)
    
    def test_kiekon_sijotus(self):
        kiekko = 1
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,]]
        paikka = self.peli.kiekon_sijotus(pelilauta, 2, 3, kiekko)
        self.assertAlmostEqual(paikka, 1)
    
    def test_seuraava_avoin_rivi(self):
        sarake = 3
        pelilauta = [[2, 1, 2, 1, 2, 1, 2,],
                     [2, 1, 2, 1, 2, 1, 2,],
                     [2, 1, 2, 1, 2, 1, 2,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 0, 0, 0, 0,]]
        avoin_rivi = self.peli.seuraava_avoin_rivi(pelilauta, sarake)
        self.assertEqual(avoin_rivi, 3)