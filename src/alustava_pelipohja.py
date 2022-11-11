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
OLIIVI = (128,128,0)

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
korkeus = (RIVIT+2) * NELION_KOKO
nayton_koko = (leveys, korkeus)
naytto = pygame.display.set_mode(nayton_koko)
fontti = pygame.font.SysFont("monospace", 100)
pelivuorot = random.randint(PELAAJA, AI)
###

###Pelilaudan alustuksia###
class Pelin_alustukset:
    """Tällä luokalla luodaan pelin pohjalle alustukset. Numpy luo taulukon
    nollista, joka on kooltaan oikean kokoinen. Taulukko käännetään käänteiseksi ('np.flip'), jotta
    kiekot putoavat pelilaudalla alas, eikä jää ylös.
    """
    def __init__(self):
        pass

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


def _pelilauta(pelilauta):
    """Pelilaudan ulkonäkö; laudan värit sekä ympyrät
    luodaan tällä funktiolla
    """
    for sarake in range(SARAKKEET):
        for rivi in range(RIVIT):
            pygame.draw.rect(naytto, SININEN,(NELION_KOKO+sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO))
            pygame.draw.circle(naytto, MIDNIGHT_B,(int(NELION_KOKO+sarake*NELION_KOKO+NELION_KOKO/2), int(rivi*NELION_KOKO+NELION_KOKO+NELION_KOKO/2)), SADE)
    
    """Luodaan pelaajan kiekko sekä AI-vastustajan kiekko
    """
    for sarake in range(SARAKKEET):
        for rivi in range(RIVIT):
            if pelilauta[rivi][sarake] == PELAAJAN_KIEKKO:
                {pygame.draw.circle(naytto, KELTAINEN,
                 (int(sarake*NELION_KOKO+NELION_KOKO/2), korkeus-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)}

            elif pelilauta[rivi][sarake] == AI_KIEKKO:
                {pygame.draw.circle(naytto, PUNAINEN,
                 (int(sarake*NELION_KOKO+NELION_KOKO/2), korkeus-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)}
    pygame.display.update()

class Nakyma:
    def __init__(self, tulos = 0):
        self.tulos  = tulos

    def _näkymä(self, näkymä, kiekko):
        vastustajan_kiekko = PELAAJAN_KIEKKO
        if kiekko == PELAAJAN_KIEKKO:
            vastustajan_kiekko == AI_KIEKKO
        
        if näkymä.count(kiekko) == 4:
            self.tulos += 100
        elif näkymä.count(kiekko) == 3 and näkymä.count(TYHJA) == 1:
            self.tulos += 5
        elif näkymä.count(kiekko) == 2 and näkymä.count(TYHJA) == 2:
            self.tulos += 2
        if näkymä.count(vastustajan_kiekko) == 3 and näkymä.count(TYHJA) == 1:
            self.tulos -= 4
        return tulos


def tulos(pelilauta, kiekko):
    tulos = 0
    """Tässä tarkistetaan keskisarakkeella onnistunut sijoitus
    """
    keski_alue = [int(i) for i in list(pelilauta[:,SARAKKEET//2])]
    laske_keski_alue = keski_alue.count(kiekko)
    tulos += laske_keski_alue * 3

    """Tässä tarkistetaan vaakasuunnassa onnistunut sijoitus
    poistetaan 3 riviä jotta saadaan laskettua neljän suora
    """
    for rivi in range(RIVIT):
        rivi_alue = [int(i) for i in list(pelilauta[rivi,:])]
        for sarake in range(SARAKKEET-3):
            näkymä_ = rivi_alue[sarake:sarake+IKKUNA]
            tulos += Nakyma._näkymä(näkymä_, kiekko)

    """Tässä tarkistetaan pystysuunnassa onnistunut sijoitus,
    iteroidaan pois 3 saraketta sekä riviä jotta
    saadaan laskettua neljän suora
    """
    for sarake in range(SARAKKEET):
        sarake_alue = [int(i) for i in list(pelilauta[:,sarake])]
        for rivi in range(RIVIT-3):
            näkymä_ = sarake_alue[rivi:rivi+IKKUNA]
            tulos += Nakyma._näkymä(näkymä_, kiekko)
    
    """ Tässä tarkistetaan diagonaalisessa suunnassa onnistunut
    sijoitus
    """
    for rivi in range(RIVIT-3):
        for sarake in range(SARAKKEET-3):
            näkymä_ = [pelilauta[rivi+i][sarake+i] for i in range(IKKUNA)]
            tulos += Nakyma._näkymä(näkymä_, kiekko)

    for rivi in range(RIVIT-3):
        for sarake in range(SARAKKEET-3):
            näkymä_ = [pelilauta[rivi+3-i][sarake+i] for i in range(IKKUNA)]
            tulos += Nakyma._näkymä(näkymä_, kiekko)


    """Funktio luo tyhjän listan johon laitetaan sellainen sarake mihin on
    mahdollista pudottaa kiekko
    """
def kiekon_sijoittaminen(pelilauta):
    kiekon_sijoitus = []
    for sarake in range(SARAKKEET):
        if Pelin_alustukset.kiekon_sijainnin_tarkistus(pelilauta, sarake):
            kiekon_sijoitus.append(sarake)
    return kiekon_sijoitus


def paras_siirto(pelilauta, kiekko):
    kiekon_sijoitus = kiekon_sijoittaminen(pelilauta)
    paras_sarake = random.choice(kiekon_sijoitus)
    paras_tulos = -10000
    for sarake in kiekon_sijoitus:
        rivi = Pelin_alustukset.seuraava_avoin_rivi(pelilauta, sarake)
        c = pelilauta.copy()
        Pelin_alustukset.kiekon_sijotus(c, rivi, sarake, kiekko)
        tulos_ = tulos(c, kiekko)
        if tulos_ > paras_tulos:
            paras_tulos = tulos_
            paras_sarake = sarake
    return paras_sarake

Peli_ohi = False
P_lauta = Pelin_alustukset.luo_pelilauta()
Pelin_alustukset.pelilaudan_tulostus(P_lauta)
_pelilauta(P_lauta)

vuoro = random.randint(PELAAJA, AI)

while not Peli_ohi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(naytto, MUSTA, (0,0, leveys, NELION_KOKO))
            x = event.pos[0]
            if vuoro == PELAAJA:
                pygame.draw.circle(naytto, OLIIVI, (x, int(NELION_KOKO/2)), SADE)
                pygame.draw.circle(naytto, KELTAINEN, (x, int(NELION_KOKO/2)), SADE-3)
        
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(naytto, MUSTA, (0,0, leveys, NELION_KOKO))
            if vuoro == PELAAJA:
                x = event.pos[0]
                sarake = int(math.floor(x/NELION_KOKO))           
                if Pelin_alustukset.kiekon_sijainnin_tarkistus(P_lauta, sarake):
                    rivi = Pelin_alustukset.seuraava_avoin_rivi(P_lauta, sarake)
                    Pelin_alustukset.kiekon_sijotus(P_lauta, rivi, sarake, PELAAJAN_KIEKKO)
                