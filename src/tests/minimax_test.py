import unittest
import numpy as np
import math
import random
from typing import List
from pelin_alustukset import minimax, KiekonSijoitus, paate_solmu, PelinAlustukset 

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2


class TestMinimax (unittest.TestCase):
    def setUp(self) -> None:
        self.minimax = minimax


    def test_minimax_ai_voitto(self):
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [1, 2, 2, 2, 2, 0, 0,]]
        a = self.minimax(pelilauta, 5, -math.inf, math.inf, True)
        ai_pisteet = 10000000000000000
        self.assertEqual(a[1], ai_pisteet)


    def test_ai_havio(self):
        syvyys = 5
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [2, 1, 1, 1, 1, 0, 0,]]
        b = self.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        ai_pisteet = -10000000000000000
        self.assertEqual(b[1], ai_pisteet)


    def test_tasuri(self):
        syvyys = 5
        pelilauta = [[1, 1, 1, 2, 2, 1, 1,], 
                     [2, 2, 1, 2, 1, 2, 2,], 
                     [2, 1, 1, 2, 2, 1, 2,], 
                     [1, 2, 2, 1, 1, 2, 1,],
                     [1, 1, 1, 2, 2, 2, 1,],
                     [1, 2, 2, 1, 2, 1, 2,]]
        c = self.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        ai_pisteet = 0
        self.assertEqual(c[1], ai_pisteet)

class TestMaxMini(unittest.TestCase):
    def setUp(self) -> None:
        self.minimax = minimax

    def test_paate_solmun_toimivuus(self):
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [1, 2, 2, 2, 2, 0, 0,]]
        self.minimax(pelilauta, 1, -math.inf, math.inf, True)
        b = paate_solmu(pelilauta)
        self.assertEqual(b, True)


    def test_palautettavat_arvot(self):
        maximizingPlayer = True
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 2, 1, 2, 1, 0, 0,],
                     [2, 1, 1, 2, 2, 1, 2,],
                     [1, 2, 2, 1, 1, 2, 1,],
                     [1, 1, 1, 2, 2, 2, 1,],
                     [1, 2, 2, 1, 2, 1, 2,]]
        d = self.minimax(pelilauta, 2, -math.inf, math.inf, maximizingPlayer)
        self.assertAlmostEqual(d[1], 0)


    def test_blokattava(self):
        pelilauta: List[List[int]] = [
             [0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 1, 2, 0, 0,],
             [2, 1, 1, 2, 1, 0, 0,],
             [2, 1, 1, 2, 2, 0, 0,]]
        sijotus =  KiekonSijoitus.kiekon_sijoittaminen(pelilauta)
        self.assertEqual(sijotus, [5,6])


class TestMinimaxies (unittest.TestCase):
    def setUp(self) -> None:
        self.minimax = minimax

    def test_maximi(self):
        pelilauta = np.zeros((RIVIT, SARAKKEET))
        e = minimax(pelilauta, 5, -10, 10, True)
        self.assertEqual(e, (3, 10))

    def test_minimi(self):
        pass