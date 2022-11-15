from pelipohja import Pelin_alustukset

SARAKKEET = 7

class KiekonSijoitus:
    def __init__(self, kiekon_sijoitus = []):
        self.kiekko_lista = kiekon_sijoitus

    """Funktio luo tyhjän listan johon laitetaan sellainen sarake mihin on
    mahdollista pudottaa kiekko
    """
    def kiekon_sijoittaminen(self, pelilauta):
        for sarake in range(SARAKKEET):
            if Pelin_alustukset.kiekon_sijainnin_tarkistus(pelilauta, sarake):
                self.kiekko_lista.append(sarake)
        return self.kiekko_lista
