import random
from pelipohja import Pelin_alustukset
from luokka_kiekon_sijotus import KiekonSijoitus
import luokka_tulos as ts

class ParasSiirto:
    def __init__(self, paras_tulos = -10000):
        self.paras_tulos = paras_tulos

    def paras_siirto(self,pelilauta, kiekko):
        kiekon_sijoitus = KiekonSijoitus.kiekon_sijoittaminen(pelilauta)
        paras_sarake = random.choice(kiekon_sijoitus)
        for sarake in kiekon_sijoitus:
            rivi = Pelin_alustukset.seuraava_avoin_rivi(pelilauta, sarake)
            c = pelilauta.copy()
            Pelin_alustukset.kiekon_sijotus(c, rivi, sarake, kiekko)
            tulos_ = ts._tulos(c, kiekko)
            if tulos_ > self.paras_tulos:
                self.paras_tulos = tulos_
                paras_sarake = sarake
        return paras_sarake
