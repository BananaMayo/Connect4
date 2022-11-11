import unittest
#import pygame
#import sys
#from alustava_pelipohja import Pelin_alustukset
from alustava_pelipohja import Nakyma
#import alustava_pelipohja as ap

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestPeli(unittest.TestCase):
    def setUp(self):
        #pygame.init()
        self.PELAAJAN_KIEKKO = 1
        self.PELAAJA = 0
        #self.pelilauta = Pelin_alustukset()
        
    """ def test_pelaajan_kiekko(self):
        if self.pelilauta[self.rivi][self.sarake] == self.PELAAJAN_KIEKKO:
            self.assertEqual(pygame.draw.circle(self.naytto, self.KELTAINEN, (int(self.sarake*self.NELION_KOKO+self.NELION_KOKO/2), self.korkeus-int(self.rivi*self.NELION_KOKO+self.NELION_KOKO/2)), self.SADE))
 """
    """ def test_seuraava_avoin_rivi(self):
        avoin_rivi = self.pelilauta.seuraava_avoin_rivi(0,0)
        for rivi in avoin_rivi:
            self.assertEqual(avoin_rivi, rivi) """
    
    def test_nakyma(self):
        kiekko = 4
        näkymä = 0
        n = Nakyma._näkymä(näkymä, kiekko)
        n.count(kiekko)
        self.assertEqual(Nakyma.tulos, 100)