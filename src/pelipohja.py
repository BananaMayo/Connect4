import random
import math
import sys
import pygame
import numpy as np
import luokka_ratkaiseva_sijotus as lrs
import luokka_tulos as lt

### Globaalit ###

# Värit
MUSTA = (0,0,0)
PUNAINEN = (178,34,34)
SININEN = (30,144,255)
MIDNIGHT_B = (25,25,112)
KELTAINEN = (255,215,0)
OLIIVI = (128,128,0)
PUU = (222,184,135)
VAALEA_KELT = (255,255,224)
RUSKEA = (139,69,19)
PUU_2 = (255,222,173)

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


#Pelilaudan alustuksia
#pylint: disable=no-self-argument
class PelinAlustukset:
    #pylint: disable=redefined-outer-name
    #pylint: disable=unsubscriptable-object
    """Tällä luokalla luodaan pelin pohjalle alustukset. Numpy luo taulukon
    nollista, joka on kooltaan oikean kokoinen. Taulukko käännetään käänteiseksi ('np.flip'), jotta
    kiekot putoavat pelilaudalla alas, eikä jää ylös.
    """
    def luo_pelilauta():
        pelilauta = np.zeros((RIVIT, SARAKKEET))
        return pelilauta

    def kiekon_sijotus(pelilauta, rivi, sarake, kiekko):
        pelilauta[rivi][sarake] = kiekko

    def kiekon_sijainnin_tarkistus(pelilauta, sarake):
        return pelilauta[RIVIT-1][sarake] == 0

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
                pygame.draw.rect(naytto, RUSKEA,(sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO), 4)
                pygame.draw.rect(naytto, PUU,(sarake*NELION_KOKO, rivi*NELION_KOKO+NELION_KOKO, NELION_KOKO, NELION_KOKO))
                pygame.draw.circle(naytto, VAALEA_KELT,(int(sarake*NELION_KOKO+NELION_KOKO/2), int(rivi*NELION_KOKO+NELION_KOKO+NELION_KOKO/2)), SADE)

        # Luodaan pelaajan kiekko sekä AI-vastustajan kiekko

        for sarake in range(SARAKKEET):
            for rivi in range(RIVIT):
                if pelilauta[rivi][sarake] == PELAAJAN_KIEKKO:
                    pygame.draw.circle(naytto, MIDNIGHT_B,(int(sarake*NELION_KOKO+NELION_KOKO/2), KORKEUS-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)

                elif pelilauta[rivi][sarake] == AI_KIEKKO:
                    pygame.draw.circle(naytto, PUNAINEN, (int(sarake*NELION_KOKO+NELION_KOKO/2), KORKEUS-int(rivi*NELION_KOKO+NELION_KOKO/2)), SADE)
        pygame.display.update()

class KiekonSijoitus:
    #pylint: disable=dangerous-default-value
    """Luokka luo tyhjän listan johon laitetaan sellainen sarake mihin on
    mahdollista pudottaa kiekko
    """
    def kiekon_sijoittaminen(pelilauta):
        kiekko_lista = []
        for sarake in range(SARAKKEET):
            if PelinAlustukset.kiekon_sijainnin_tarkistus(pelilauta, sarake):
                kiekko_lista.append(sarake)
        return kiekko_lista

def paate_solmu(pelilauta):
        return voitto_siirto.ratkaiseva_sijotus(pelilauta, PELAAJAN_KIEKKO) or voitto_siirto.ratkaiseva_sijotus(pelilauta, AI_KIEKKO) or len(KiekonSijoitus.kiekon_sijoittaminen(pelilauta)) == 0

voitto_siirto = lrs.RatkaisevaSijotus
tulos = lt.Tulos
class MiniMax:
    """Minimax-algoritmi AI-tekoälyä varten. Luokkassa käytetään alpha-beta karsintaa
    jonka takia funktiossa on määriteltynä 'alpha' ja 'beta'.
    """
    def minimax(pelilauta, syvyys, alpha, beta, maximizingPlayer):
        sallittu_sijotus = KiekonSijoitus.kiekon_sijoittaminen(pelilauta)
        on_paate_solmu = paate_solmu(pelilauta)
        if syvyys == 0 or on_paate_solmu:
            if on_paate_solmu:
                if voitto_siirto.ratkaiseva_sijotus(pelilauta, AI_KIEKKO):
                    return (None, 10000000000000000)
                elif voitto_siirto.ratkaiseva_sijotus(pelilauta, PELAAJAN_KIEKKO):
                    return (None, -10000000000000000)
                else:
                    return (None, 0)
            else:
                return (None, tulos.tulos_(pelilauta, AI_KIEKKO))
        #MaximizingPlayer osio
        if maximizingPlayer:
            satun_sarake = random.choice(sallittu_sijotus)
            nykyinen_arvo = -math.inf
            for sarake in sallittu_sijotus:
                rivi = PelinAlustukset.seuraava_avoin_rivi(pelilauta, sarake)
                lauta_kopio = pelilauta.copy()
                PelinAlustukset.kiekon_sijotus(lauta_kopio, rivi, sarake, AI_KIEKKO)
                uusi_tulos = MiniMax.minimax(lauta_kopio, syvyys-1, alpha, beta, False)[1]
                if uusi_tulos > nykyinen_arvo:
                    nykyinen_arvo = uusi_tulos
                    satun_sarake = sarake
                alpha = max(alpha, nykyinen_arvo)
                if alpha >= beta:
                    break
            return satun_sarake, nykyinen_arvo
        #MinimizingPlayer osio
        else:
            nykyinen_arvo = math.inf
            satun_sarake = random.choice(sallittu_sijotus)
            for sarake in sallittu_sijotus:
                rivi = PelinAlustukset.seuraava_avoin_rivi(pelilauta, sarake)
                lauta_kopio = pelilauta.copy()
                PelinAlustukset.kiekon_sijotus(lauta_kopio, rivi, sarake, PELAAJAN_KIEKKO)
                uusi_tulos = MiniMax.minimax(lauta_kopio, syvyys-1, alpha, beta, True)[1]
                if uusi_tulos < nykyinen_arvo:
                    nykyinen_arvo = uusi_tulos
                    satun_sarake = sarake
                beta = min(beta, nykyinen_arvo)
                if alpha >= beta:
                    break
            return satun_sarake, nykyinen_arvo

# PYGAME alustukset
P_lauta = PelinAlustukset.luo_pelilauta()
PelinAlustukset.pelilaudan_tulostus(P_lauta)
PELI_OHI = False

pygame.init()

LEVEYS = (SARAKKEET * NELION_KOKO)
KORKEUS = (RIVIT+1) * NELION_KOKO
nayton_koko = (LEVEYS, KORKEUS)

naytto = pygame.display.set_mode((nayton_koko))
pygame.display.set_caption('CONNECT4')
Pelilauta.pelilauta_(P_lauta)
pygame.display.update()

fontti = pygame.font.SysFont("monospace", 100)
#pelivuorot = random.randint(PELAAJA, AI)

vuoro = random.randint(PELAAJA, AI)


"""Tämä osio kattaa pelin tapahtumat silloin kun 
peli on käynnissä, ts. kun peliä ei ole vielä voitettu
jomman kumman osapuolen toimesta
"""
while not PELI_OHI:
    #alustetaan pelin sulkeminen 'system-exitillä', eli kun pelin aikana pelaaja 
    #painaa punaista exit-painiketta peli sammuu

    for event in pygame.event.get():
        #pylint: disable=no-member
        if event.type == pygame.QUIT:
            sys.exit()

        #Tämä osio näyttää pelaajan kiekon ylärivillä kun on hänen vuoro
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(naytto, PUU_2, (0,0, LEVEYS, NELION_KOKO))
            #x = event.pos[0]
            if vuoro == PELAAJA:
                #pygame.draw.circle(naytto, OLIIVI, (x, int(NELION_KOKO/2)), SADE)
                pygame.draw.circle(naytto, MIDNIGHT_B, (LEVEYS//2, NELION_KOKO//2), SADE)

        pygame.display.update()

        #Tämä osio määrittelee mitä tapahtuu hiiren napin painalluksesta, ts. tiputtaa kiekon
        #sarakkeeseen johon on 'klikattu', mikäli se on sallittu sarake (ei täynnä)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(naytto, PUU_2, (0,0, LEVEYS, NELION_KOKO))
            if vuoro == PELAAJA:
                x = event.pos[0]
                sarake = int(math.floor(x/NELION_KOKO))
                if PelinAlustukset.kiekon_sijainnin_tarkistus(P_lauta, sarake):
                    rivi = PelinAlustukset.seuraava_avoin_rivi(P_lauta, sarake)
                    PelinAlustukset.kiekon_sijotus(P_lauta, rivi, sarake, PELAAJAN_KIEKKO)
                    
                    # Jos pelaaja tekee ratkaisevan sijoituksen lopetetaan peli
                    if lrs.RatkaisevaSijotus.ratkaiseva_sijotus(P_lauta, PELAAJAN_KIEKKO):
                        #Muista laittaa tekstiä peliin!#
                        PELI_OHI = True
                    vuoro +=1
                    vuoro = vuoro%2
                    PelinAlustukset.pelilaudan_tulostus(P_lauta)
                    Pelilauta.pelilauta_(P_lauta)
        pygame.display.update()

    if vuoro == AI and not PELI_OHI:
        # SYVYYS = 5, vaikeustasoa voi muokata vaihtamalla syvyyttä, mitä syvemmälle algoritmi etsii
        # sitä vaikeammaksi tekoäly muuttuu
        sarake, MiniMax_pisteytys = MiniMax.minimax(P_lauta, 5, -math.inf, math.inf, True)
        if PelinAlustukset.kiekon_sijainnin_tarkistus(P_lauta, sarake):
            rivi = PelinAlustukset.seuraava_avoin_rivi(P_lauta, sarake)
            #Pudotetaan tekoälyn kiekko
            PelinAlustukset.kiekon_sijotus(P_lauta, rivi, sarake, AI_KIEKKO)

            #Jos tekoäly tekee ratkaisevan sijoituksen lopetetaan peli
            if lrs.RatkaisevaSijotus.ratkaiseva_sijotus(P_lauta, AI_KIEKKO):
                PELI_OHI = True
            PelinAlustukset.pelilaudan_tulostus(P_lauta)
            Pelilauta.pelilauta_(P_lauta)
            vuoro +=1
            vuoro = vuoro%2

    if PELI_OHI is True:
        pygame.time.wait(4000)
