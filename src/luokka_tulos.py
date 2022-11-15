from luokka_nakyma import Nakyma

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4

class Tulos:
    """Luokalla tarkistetaan eri suuntaiset sijoitukset
    """
    def __init__(self, tulos = 0):
        self.tulos = tulos

    def _tulos(self, pelilauta, kiekko):
        """Tässä tarkistetaan keskisarakkeella onnistunut sijoitus
        """
        keski_alue = [int(i) for i in list(pelilauta[:,SARAKKEET//2])]
        laske_keski_alue = keski_alue.count(kiekko)
        self.tulos += laske_keski_alue * 3

        """Tässä tarkistetaan vaakasuunnassa onnistunut sijoitus
        """
        for rivi in range(RIVIT):
            rivi_alue = [int(i) for i in list(pelilauta[rivi,:])]
            for sarake in range(SARAKKEET-3):
                näkymä_ = rivi_alue[sarake:sarake+IKKUNA]
                self.tulos += Nakyma._näkymä(näkymä_, kiekko)

        """Tässä tarkistetaan pystysuunnassa onnistunut sijoitus
        """
        for sarake in range(SARAKKEET):
            sarake_alue = [int(i) for i in list(pelilauta[:,sarake])]
            for rivi in range(RIVIT-3):
                näkymä_ = sarake_alue[rivi:rivi+IKKUNA]
                self.tulos += Nakyma._näkymä(näkymä_, kiekko)

        """ Tässä tarkistetaan diagonaalisessa suunnassa onnistunut
        sijoitus
        """
        for rivi in range(RIVIT-3):
            for sarake in range(SARAKKEET-3):
                näkymä_ = [pelilauta[rivi+i][sarake+i] for i in range(IKKUNA)]
                self.tulos += Nakyma._näkymä(näkymä_, kiekko)

        for rivi in range(RIVIT-3):
            for sarake in range(SARAKKEET-3):
                näkymä_ = [pelilauta[rivi+3-i][sarake+i] for i in range(IKKUNA)]
                self.tulos += Nakyma._näkymä(näkymä_, kiekko)
