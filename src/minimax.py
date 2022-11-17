from luokka_kiekon_sijotus import KiekonSijoitus
from luokka_ratkaiseva_sijotus import RatkaisevaSijotus
from luokka_tulos import Tulos
# Pelaajan kiekko, tekoälyn kiekko
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2
TYHJA = 0

voitto_siirto = RatkaisevaSijotus.ratkaiseva_sijotus()
siirto = KiekonSijoitus.kiekon_sijoittaminen()
tulos = Tulos.tulos_()

def paate_solmu(pelilauta):
        return voitto_siirto(pelilauta, PELAAJAN_KIEKKO) or voitto_siirto(pelilauta, AI_KIEKKO) or len(siirto(pelilauta)) == 0

class MiniMax:
    """Minimax-algoritmi AI-tekoälyä varten. Luokkassa käytetään alpha-beta karsintaa
    jonka takia funktiossa on määriteltynä 'alpha' ja 'beta'.
    """
    def minimax(pelilauta, syvyys, alpha, beta, maximizingPlayer):
        salittu_sijotus = siirto(pelilauta)
        on_paate_solmu = paate_solmu(pelilauta)
        if syvyys == 0 or on_paate_solmu:
            if on_paate_solmu:
                if voitto_siirto(pelilauta, AI_KIEKKO):
                    return (None, 10000000000000000)
                elif voitto_siirto(pelilauta, PELAAJAN_KIEKKO):
                    return (None, -10000000000000000)
                else:
                    return (None, 0)
            else:
                return (None, tulos(pelilauta, AI_KIEKKO))
