import random
import math
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
#pylint: disable=invalid-name
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
        return pelilauta[rivi][sarake]

    def kiekon_sijainnin_tarkistus(pelilauta, sarake):
        return pelilauta[RIVIT-1][sarake] == 0

    def seuraava_avoin_rivi(pelilauta, sarake):
        for rivi in range(RIVIT):
            if pelilauta[rivi][sarake] == 0:
                return rivi

    def pelilaudan_tulostus(pelilauta):
        print(np.flip(pelilauta, 0))

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

#Päätesolmun määrittely, tarkoittaa viimeistä solmua. Peli päättyy päätesolmuun, tai kun syvyys on 0
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
