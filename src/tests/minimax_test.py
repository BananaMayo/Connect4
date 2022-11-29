import unittest
import math
import pygame
from typing import List
from pelin_alustukset import MiniMax

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestMinimax (unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_minimax_ai_voitto(self):
        pygame.init()
        minimax = MiniMax
        syvyys = 5
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [1, 2, 2, 2, 2, 0, 0,]]

        a = minimax.minimax(pelilauta, syvyys, -math.inf, math.inf, True)
        ai_pisteet = 10000000000000000
        self.assertEqual(a[1], ai_pisteet)
    
    def test_ai_havio(self):
        pygame.init()
        self.minimax = MiniMax
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
        pygame.init()
        self.minimax = MiniMax
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

"""     def test_true_arvo(self):
        pelilauta= [[0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 0, 0, 0, 0,],
                    [0, 0, 0, 2, 0, 0, 0,],
                    [0, 0, 1, 1, 2, 0, 0,]]
        mini = MiniMax.minimax(pelilauta, 5, -math.inf, math.inf, maximizingPlayer=True)
        self.assertAlmostEqual(mini, True) """


