import unittest
from luokka_nakyma import Nakyma

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestNakyma(unittest.TestCase):
    def setUp(self):
        self.PELAAJAN_KIEKKO = 1
        self.PELAAJA = 0
        self.näkymä = Nakyma(0)
        
    def test_nakyma(self):
        näkymä = []
        a = Nakyma._näkymä(1,näkymä,4)
        self.assertEqual(a, 100)

""" def test_pelaajan_kiekko(self):
    if self.pelilauta[self.rivi][self.sarake] == self.PELAAJAN_KIEKKO:
        self.assertEqual(pygame.draw.circle(self.naytto, self.KELTAINEN, (int(self.sarake*self.NELION_KOKO+self.NELION_KOKO/2), self.korkeus-int(self.rivi*self.NELION_KOKO+self.NELION_KOKO/2)), self.SADE))
"""
""" def test_seuraava_avoin_rivi(self):
    avoin_rivi = self.pelilauta.seuraava_avoin_rivi(0,0)
    for rivi in avoin_rivi:
        self.assertEqual(avoin_rivi, rivi) """
