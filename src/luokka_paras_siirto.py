import random
from pelipohja import PelinAlustukset
from luokka_kiekon_sijotus import KiekonSijoitus
import luokka_tulos as ts

class ParasSiirto:
    def __init__(self, paras_tulos = -10000):
        self.paras_tulos = paras_tulos

    def paras_siirto(self, pelilauta, kiekko):
        kiekon_sijoitus = KiekonSijoitus.kiekon_sijoittaminen(pelilauta)
        paras_sarake = random.choice(kiekon_sijoitus)
        for sarake in kiekon_sijoitus:
            rivi = PelinAlustukset.seuraava_avoin_rivi(pelilauta, sarake)
            kopio = pelilauta.copy()
            PelinAlustukset.kiekon_sijotus(kopio, rivi, sarake, kiekko)
            tulos = ts.Tulos.tulos_(kopio, kiekko)
            if tulos > self.paras_tulos:
                self.paras_tulos = tulos
                paras_sarake = sarake
        return paras_sarake
