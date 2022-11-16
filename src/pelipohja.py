import random
import math
import sys
import pygame
import numpy as np
import luokka_ratkaiseva_sijotus as rs

### Globaalit ###

# Värit
MUSTA = (0,0,0)
PUNAINEN = (178,34,34)
SININEN = (30,144,255)
MIDNIGHT_B = (25,25,112)
KELTAINEN = (255,215,0)
OLIIVI = (128,128,0)

# Pelin rakenne (rivit ja sarakkeet)
RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4

# Pelaaja ja tekoäly
PELAAJA = 0
AI = 1

# Pelaajan kiekko, tekoälyn kiekko
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2
TYHJA = 0

# PYGAME alustukset
pygame.init()
LEVEYS = (NELION_KOKO+SARAKKEET * NELION_KOKO+NELION_KOKO)
KORKEUS = (RIVIT+2) * NELION_KOKO
nayton_koko = (LEVEYS, KORKEUS)
naytto = pygame.display.set_mode(nayton_koko)
fontti = pygame.font.SysFont("monospace", 100)
pelivuorot = random.randint(PELAAJA, AI)


# Pelilaudan alustuksia

#pylint: disable=no-self-argument

class PelinAlustukset:
    #pylint: disable=redefined-outer-name
    #pylint: disable=unsubscriptable-object
    """Tällä luokalla luodaan pelin pohjalle alustukset. Numpy luo taulukon
    nollista, joka on kooltaan oikean kokoinen. Taulukko käännetään käänteiseksi ('np.flip'), jotta
    kiekot putoavat pelilaudalla alas, eikä jää ylös.
    """
    def luo_pelilauta():
        pelilauta = np.zeros((RIVIT, SARAKKEET+1))#huom! tämä leventää pelilautaa, poista jos on ongelmia!#
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


class Pelilauta:
    def pelilauta_(pelilauta):
        """Pelilaudan ulkonäkö; laudan värit sekä ympyrät
        luodaan tällä funktiolla
        """
        for sarake in range(SARAKKEET):
            for rivi in range(RIVIT):
                pygame.draw.rect(naytto, SININEN,(NELION_KOKO+sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO))
                pygame.draw.circle(naytto, MIDNIGHT_B,(int(NELION_KOKO+sarake*NELION_KOKO+NELION_KOKO/2), int(rivi*NELION_KOKO+NELION_KOKO+NELION_KOKO/2)), SADE)

        # Luodaan pelaajan kiekko sekä AI-vastustajan kiekko

        for sarake in range(SARAKKEET):
            for rivi in range(RIVIT):
                if pelilauta[rivi][sarake] == PELAAJAN_KIEKKO:
                    {pygame.draw.circle(naytto, KELTAINEN,
                    (int(sarake*NELION_KOKO+NELION_KOKO/2), KORKEUS-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)}

                elif pelilauta[rivi][sarake] == AI_KIEKKO:
                    {pygame.draw.circle(naytto, PUNAINEN,
                    (int(sarake*NELION_KOKO+NELION_KOKO/2), KORKEUS-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)}
    pygame.display.update()

P_lauta = PelinAlustukset.luo_pelilauta()
PelinAlustukset.pelilaudan_tulostus(P_lauta)
Pelilauta.pelilauta_(P_lauta)
PELI_OHI = False
pygame.display.update()
vuoro = random.randint(PELAAJA, AI)


while not PELI_OHI:
    for event in pygame.event.get():
        #pylint: disable=no-member
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(naytto, MUSTA, (0,0, LEVEYS, NELION_KOKO))
            x = event.pos[0]
            if vuoro == PELAAJA:
                pygame.draw.circle(naytto, OLIIVI, (x, int(NELION_KOKO/2)), SADE)
                pygame.draw.circle(naytto, KELTAINEN, (x, int(NELION_KOKO/2)), SADE-3)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(naytto, MUSTA, (0,0, LEVEYS, NELION_KOKO))
            if vuoro == PELAAJA:
                x = event.pos[0]
                sarake = int(math.floor(x/NELION_KOKO))
                if PelinAlustukset.kiekon_sijainnin_tarkistus(P_lauta, sarake):
                    rivi = PelinAlustukset.seuraava_avoin_rivi(P_lauta, sarake)
                    PelinAlustukset.kiekon_sijotus(P_lauta, rivi, sarake, PELAAJAN_KIEKKO)

                    if rs.RatkaisevaSijotus.ratkaiseva_sijotus(P_lauta, PELAAJAN_KIEKKO):
                        #Muista laittaa tekstiä peliin!#
                        PELI_OHI = True
                    vuoro +=1
                    vuoro = vuoro%2
                    PelinAlustukset.luo_pelilauta(P_lauta)
                    Pelilauta.pelilauta_(P_lauta)
        pygame.display.update()

    if PELI_OHI is True:
        pygame.time.wait(4000)
