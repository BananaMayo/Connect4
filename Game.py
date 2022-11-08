### Import osio ###
import pygame
import sys
import math
import random
import numpy as np

### Globaalit ###

#Värit
MUSTA = (0,0,0)
PUNAINEN = (178,34,34)
SININEN = (65,105,225)
KELTAINEN = (255,215,0)

#Pelin rakenne (rivit ja sarakkeet)
RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4

#Pelaaja ja tekoäly
PELAAJA = 0
AI = 1

#Pelaajan kiekko, tekoälyn kiekko
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2
TYHJA = 0

##PYGAME
pygame.init()
leveys = SARAKKEET * NELION_KOKO
korkeus = (RIVIT+1) * NELION_KOKO
nayton_koko = (leveys, korkeus)
naytto = pygame.display.set_mode(nayton_koko)
fontti = pygame.font.SysFont()
pelivuorot = random.randint(PELAAJA, AI)
###


def luo_pelilauta():
    pelilauta = np.zeros((RIVIT, SARAKKEET))
    return pelilauta

def kiekon_sijotus(pelilauta, rivi, sarake, kiekko):
    pelilauta[rivi][sarake] = kiekko

def kiekon_sijainnin_tarkistus(pelilauta, sarake):
    return pelilauta[RIVIT-1][sarake]

def seuraava_avoin_rivi(pelilauta, sarake):
    for rivi in range(RIVIT):
        if pelilauta[rivi][sarake] == 0:
            return rivi

def pelilaudan_tulostus(pelilauta):
    print(np.flip(pelilauta, 0))


### PYGAME pelilaudan teko


def pelilauta(pelilauta):
    for sarake in range(SARAKKEET):
        for rivi in range(RIVIT):
            pygame.draw.rect(naytto, SININEN, (sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO))
            pygame.draw.circle(naytto, MUSTA, (int(sarake*NELION_KOKO+NELION_KOKO/2), int(rivi*NELION_KOKO+NELION_KOKO+NELION_KOKO/2)), SADE)
    
    