import unittest
import math
from typing import List
from pelin_alustukset import MiniMax

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestMinimax (unittest.TestCase):
    def setUp(self) -> None:
        self.minimax = MiniMax

    def test_minimax_ai_voitto(self):
        syvyys = 5
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [1, 2, 2, 2, 2, 0, 0,]]

        a = self.minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
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
        b = self.minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
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
        c = self.minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        ai_pisteet = 0
        self.assertEqual(c[1], ai_pisteet)
    

    ## Keskeneräinen
    def test_palautettavat_arvot(self):
        maximizingPlayer = True
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 2, 1, 2, 1, 0, 0,],
                     [2, 1, 1, 2, 2, 1, 2,],
                     [1, 2, 2, 1, 1, 2, 1,],
                     [1, 1, 1, 2, 2, 2, 1,],
                     [1, 2, 2, 1, 2, 1, 2,]]
        d = self.minimax.minimax(pelilauta, 2, -math.inf, math.inf, maximizingPlayer)

        self.assertAlmostEqual(d[1], 0)


    ## Koitan testata Maximizing- ja Minimizingplayer osioita, vielä vähän vaikeuksia sen kanssa
    def test_true_arvo(self):
        pelilauta= list([[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0]])
        mini = MiniMax.minimax(list(pelilauta), 5, -math.inf, math.inf, maximizingPlayer=True)
        self.assertAlmostEqual(mini, 3)


