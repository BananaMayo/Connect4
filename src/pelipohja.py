import random
import math
import time
import sys
import pygame
from pelin_alustukset import PelinAlustukset
from pelin_alustukset import MiniMax
import luokka_ratkaiseva_sijotus as lrs

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

#pylint: disable=no-self-argument
#pylint: disable=invalid-name
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

# PYGAME alustukset
P_lauta = PelinAlustukset.luo_pelilauta()
PelinAlustukset.pelilaudan_tulostus(P_lauta)
#pylint: disable=no-member
pygame.init()

LEVEYS = (SARAKKEET * NELION_KOKO)
KORKEUS = (RIVIT+1) * NELION_KOKO
nayton_koko = (LEVEYS, KORKEUS)

naytto = pygame.display.set_mode((nayton_koko))
pygame.display.set_caption('CONNECT4')
Pelilauta.pelilauta_(P_lauta)
pygame.display.update()

fontti = pygame.font.SysFont("Helvetica", 48)
pelivuorot = random.randint(PELAAJA, AI)


class Pelaa:
    """Tämä luokka kattaa pelin tapahtumat silloin kun
    peli on käynnissä, ts. kun peliä ei ole vielä voitettu
    jomman kumman osapuolen toimesta
    """
    def start():
        #alku = time.time()
        PELI_OHI = False
        vuoro = random.randint(PELAAJA, AI)
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
                                tekstia = fontti.render("Voitit, hienoa!!!", 1, MIDNIGHT_B)
                                naytto.blit(tekstia, (220,25))
                                PELI_OHI = True
                            vuoro +=1
                            vuoro = vuoro%2
                            PelinAlustukset.pelilaudan_tulostus(P_lauta)
                            Pelilauta.pelilauta_(P_lauta)
                pygame.display.update()
            #pylint: disable=unused-variable
            if vuoro == AI and not PELI_OHI:
                # Tässä määritetään vastustaja (AI) jossa käytetään Minimax-algoritmia
                # SYVYYS = 5, vaikeustasoa voi muokata vaihtamalla syvyyttä, mitä syvemmälle algoritmi etsii
                # sitä vaikeammaksi tekoäly muuttuu
                sarake, MiniMax_pisteytys = MiniMax.minimax(P_lauta, 5, -math.inf, math.inf, True)
                alku_max = time.time()
                if PelinAlustukset.kiekon_sijainnin_tarkistus(P_lauta, sarake):
                    rivi = PelinAlustukset.seuraava_avoin_rivi(P_lauta, sarake)
                    #Pudotetaan tekoälyn kiekko
                    PelinAlustukset.kiekon_sijotus(P_lauta, rivi, sarake, AI_KIEKKO)
                    loppu_max = time.time()
                    aika = (loppu_max-alku_max)
                    print("AI:n kiekon sijottamisessa kului",aika,"s")

                    #Jos tekoäly tekee ratkaisevan sijoituksen lopetetaan peli
                    if lrs.RatkaisevaSijotus.ratkaiseva_sijotus(P_lauta, AI_KIEKKO):
                        tekstia_2 = fontti.render("Harmi, uudestaan vaan...", 1, PUNAINEN)
                        naytto.blit(tekstia_2, (78,15))
                        PELI_OHI = True
                    PelinAlustukset.pelilaudan_tulostus(P_lauta)
                    Pelilauta.pelilauta_(P_lauta)
                    vuoro +=1
                    vuoro = vuoro%2

            if PELI_OHI is True:
                pygame.time.wait(4000)
