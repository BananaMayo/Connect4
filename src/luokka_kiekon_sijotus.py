from pelipohja import PelinAlustukset

SARAKKEET = 7

class KiekonSijoitus:
    #pylint: disable=dangerous-default-value
    """Luokka luo tyhjän listan johon laitetaan sellainen sarake mihin on
    mahdollista pudottaa kiekko
    """
    def kiekon_sijoittaminen(self, pelilauta):
        kiekko_lista = []
        for sarake in range(SARAKKEET):
            if PelinAlustukset.kiekon_sijainnin_tarkistus(pelilauta, sarake):
                kiekko_lista.append(sarake)
        return kiekko_lista
