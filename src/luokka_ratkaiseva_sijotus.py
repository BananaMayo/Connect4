#pylint: disable=no-self-argument
#pylint: disable=inconsistent-return-statements
#pylint: disable=unsubscriptable-object
#pylint: disable=pointless-string-statement

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
IKKUNA = 4
SADE = int(NELION_KOKO/2 - 5)
ARVO = True


class RatkaisevaSijotus:
    """Luokan funktio tarkistaa erikseen neljän suoran laudalla, sisältää
    pysty-, vaaka- ja digaonaaliset suunnat. Mikäli neljän suora on saavutettu
    palautetaan arvo 'True'
    """
    def ratkaiseva_sijotus(pelilauta, kiekko):
        # Vaakasuorassa saatu neljän suoran tarkistus:
        for sarake in range(SARAKKEET-3):
            for rivi in range(RIVIT):
                if pelilauta[rivi][sarake] == kiekko and pelilauta[rivi][sarake+1] == kiekko and pelilauta[rivi][sarake+2] == kiekko and pelilauta[rivi][sarake+3]==kiekko:
                    return ARVO
        # Pystysuorassa saatu neljän suoran tarkistus:
        for sarake in range(SARAKKEET):
            for rivi in range(RIVIT-3):
                if pelilauta[rivi][sarake] == kiekko and pelilauta[rivi+1][sarake] == kiekko and pelilauta[rivi+2][sarake] == kiekko and pelilauta[rivi+3][sarake]==kiekko:
                    return ARVO
        # Diagonaalisessa suunnassa saatu neljän suora:
        for sarake in range(SARAKKEET-3):
            for rivi in range(RIVIT-3):
                if pelilauta[rivi][sarake] == kiekko and pelilauta[rivi+1][sarake+1] == kiekko and pelilauta[rivi+2][sarake+2] == kiekko and pelilauta[rivi+3][sarake+3]==kiekko:
                    return ARVO
        for sarake in range(SARAKKEET-3):
            for rivi in range(3,RIVIT):
                if pelilauta[rivi][sarake] == kiekko and pelilauta[rivi-1][sarake+1] == kiekko and pelilauta[rivi-2][sarake+2] == kiekko and pelilauta[rivi-3][sarake+3]==kiekko:
                    return ARVO
