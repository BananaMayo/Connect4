import unittest
from luokka_ratkaiseva_sijotus import RatkaisevaSijotus

class TestSijotus(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    #pystysuora neljän suora
    def test_pelaaja_true_arvo(self):
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 2, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 2, 1, 2, 0, 0,],
                     [2, 0, 2, 1, 1, 0, 0,]]
        kiekko = 1
        sijotus = RatkaisevaSijotus.ratkaiseva_sijotus(pelilauta, kiekko)
        self.assertEqual(sijotus, True)

    #diagonaalinen neljän suora (pos)
    def test_ai_true_arvo1(self):
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 2, 0,],
                     [0, 0, 0, 2, 2, 1, 0,],
                     [0, 0, 0, 2, 1, 2, 0,],
                     [1, 2, 2, 1, 2, 1, 0,]]
        kiekko = 2
        sijotus = RatkaisevaSijotus.ratkaiseva_sijotus(pelilauta, kiekko)
        self.assertEqual(sijotus, True)

    #diagonaalinen neljän suora (neg)
    def test_ai_true_arvo2(self):
        pelilauta = [[0, 0, 0, 0, 0, 0, 0,],
                     [0, 0, 0, 1, 0, 0, 0,],
                     [0, 0, 2, 1, 0, 1, 0,],
                     [0, 0, 1, 2, 2, 1, 0,],
                     [0, 0, 2, 2, 2, 1, 0,],
                     [1, 2, 2, 1, 1, 2, 0,]]
        kiekko = 2
        sijotus = RatkaisevaSijotus.ratkaiseva_sijotus(pelilauta, kiekko)
        self.assertEqual(sijotus, True)
