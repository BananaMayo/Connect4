import unittest
import math
from pelipohja import MiniMax, MiniMax_pisteytys

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestMinimax (unittest.TestCase):
    def setup(self):
        self.alpha = max()
        self.beta = min()

    def test_minimax_ai_voitto(self):
        self.minimax = MiniMax
        self.pisteet = MiniMax_pisteytys
        syvyys = 5
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 1, 0, 0, 0,],
        [0, 0, 0, 1, 0, 0, 0,],
        [0, 0, 0, 2, 0, 0, 0,],
        [0, 0, 0, 1, 0, 0, 0,],
        [1, 2, 2, 2, 2, 0, 0,]]
        self.minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        ai_pisteet = 10000000000000000
        self.assertEqual(self.pisteet, ai_pisteet)
    
    """ def test_ai_aloituspisteet(self):
        self.minimax = MiniMax
        self.pisteet = MiniMax_pisteytys
        syvyys = 5
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 2, 0, 0, 0,]]
        self.minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        while True:
            for sarake in range(SARAKKEET):
                for rivi in range(RIVIT):
                    if pelilauta[rivi][sarake].count(2) == 1:
                        break
                    ai_pisteet = 40
                    self.assertEqual(self.pisteet, ai_pisteet) """