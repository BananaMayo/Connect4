from pelipohja import PelinAlustukset

SARAKKEET = 7

class KiekonSijoitus:
    #pylint: disable=dangerous-default-value
    """Luokka luo tyhjän listan johon laitetaan sellainen sarake mihin on
    mahdollista pudottaa kiekko
    """
    def __init__(self, kiekon_sijoitus = []):
        self.kiekko_lista = kiekon_sijoitus

    def kiekon_sijoittaminen(self, pelilauta):
        for sarake in range(SARAKKEET):
            if PelinAlustukset.kiekon_sijainnin_tarkistus(pelilauta, sarake):
                self.kiekko_lista.append(sarake)
        return self.kiekko_lista
