from luokka_nakyma import Nakyma

RIVIT = 6
SARAKKEET = 7
IKKUNA = 4
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
#pylint: disable=no-self-argument
class Tulos:
    #pylint: disable=unsubscriptable-object
    """Luokalla tarkistetaan eri suuntaiset sijoitukset
    """
    def tulos_(pelilauta, kiekko):
        tulos = 0
        # Tässä tarkistetaan keskisarakkeella onnistunut sijoitus

        keski_alue = [int(i) for i in list(pelilauta[:,SARAKKEET//2])]
        laske_keski_alue = keski_alue.count(kiekko)
        tulos += laske_keski_alue * 3

        # Tässä tarkistetaan vaakasuunnassa onnistunut sijoitus

        for rivi in range(RIVIT):
            rivi_alue = [int(i) for i in list(pelilauta[rivi,:])]
            for sarake in range(SARAKKEET-3):
                näkymä_ = rivi_alue[sarake:sarake+IKKUNA]
                tulos += Nakyma.nakyma_(näkymä_, kiekko)

        # Tässä tarkistetaan pystysuunnassa onnistunut sijoitus

        for sarake in range(SARAKKEET):
            sarake_alue = [int(i) for i in list(pelilauta[:,sarake])]
            for rivi in range(RIVIT-3):
                näkymä_ = sarake_alue[rivi:rivi+IKKUNA]
                tulos += Nakyma.nakyma_(näkymä_, kiekko)

        # Tässä tarkistetaan diagonaalisessa suunnassa onnistunut sijoitus

        for rivi in range(RIVIT-3):
            for sarake in range(SARAKKEET-3):
                näkymä_ = [pelilauta[rivi+i][sarake+i] for i in range(IKKUNA)]
                tulos += Nakyma.nakyma_(näkymä_, kiekko)

        for rivi in range(RIVIT-3):
            for sarake in range(SARAKKEET-3):
                näkymä_ = [pelilauta[rivi+3-i][sarake+i] for i in range(IKKUNA)]
                tulos += Nakyma.nakyma_(näkymä_, kiekko)
        return tulos
