import unittest
import pygame
import sys
from alustava_pelipohja import pelilauta

class TestPelaaja(unittest.TestCase):
    def setUp(self):
        self.click = False
        pygame.init()
        self.PELAAJAN_KIEKKO = 1
        self.PELAAJA = 0
        self.pelilauta = pelilauta()
        
    def test_pelaajan_kiekko(self):
        if self.pelilauta[self.rivi][self.sarake] == self.PELAAJAN_KIEKKO:
            self.assertEqual(pygame.draw.circle(self.naytto, self.KELTAINEN, (int(self.sarake*self.NELION_KOKO+self.NELION_KOKO/2), self.korkeus-int(self.rivi*self.NELION_KOKO+self.NELION_KOKO/2)), self.SADE))


"""     def test_main_to_game(self):
        mx, my = pygame.mouse.get_pos()
        self.game1_button = pygame.Rect(245, 120, 150, 30)
        if self.game1_button.collidepoint((mx, my)):
            if self.click:
               self.assertEqual(self.labyrinth.on_execute()) """