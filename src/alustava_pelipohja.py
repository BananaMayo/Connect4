### Import osio ###
import random
import pygame
import sys
import numpy as np
import math
###

### Globaalit ###

#Värit
MUSTA = (0,0,0)
PUNAINEN = (178,34,34)
SININEN = (30,144,255)
MIDNIGHT_B = (25,25,112)
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

##PYGAME alustukset
pygame.init()
leveys = NELION_KOKO+SARAKKEET * NELION_KOKO+NELION_KOKO
korkeus = (RIVIT+1) * NELION_KOKO
nayton_koko = (leveys, korkeus)
naytto = pygame.display.set_mode(nayton_koko)
fontti = pygame.font.SysFont("monospace", 100)
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
    """Pelilaudan ulkonäkö; laudan värit sekä ympyrät
    luodaan tällä funktiolla

    Args:
        pelilauta (_type_): _description_
    """
    for sarake in range(SARAKKEET):
        for rivi in range(RIVIT):
            pygame.draw.rect(naytto, SININEN, (NELION_KOKO+sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO))
            pygame.draw.circle(naytto, MIDNIGHT_B, (int(NELION_KOKO+sarake*NELION_KOKO+NELION_KOKO/2), int(rivi*NELION_KOKO+NELION_KOKO+NELION_KOKO/2)), SADE)
    
    """Luodaan pelaajan kiekko sekä AI-vastustajan kiekko
    """
    for sarake in range(SARAKKEET):
        for rivi in range(RIVIT):
            if pelilauta[rivi][sarake] == PELAAJAN_KIEKKO:
                pygame.draw.circle(naytto, KELTAINEN, (int(sarake*NELION_KOKO+NELION_KOKO/2), korkeus-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)
            elif pelilauta[rivi][sarake] == AI_KIEKKO:
                pygame.draw.circle(naytto, PUNAINEN, (int(sarake*NELION_KOKO+NELION_KOKO/2), korkeus-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)
    pygame.display.update()

Peli_ohi = False
P_lauta = luo_pelilauta()
pelilaudan_tulostus(P_lauta)
pelilauta(P_lauta)

vuoro = random.randint(PELAAJA, AI)

while not Peli_ohi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(naytto, MUSTA, (0,0, leveys, NELION_KOKO))
            x = event.pos[0]
            if vuoro == PELAAJA:
                pygame.draw.circle(naytto, KELTAINEN, (x, int(NELION_KOKO/2)), SADE)
        pygame.display.update()


