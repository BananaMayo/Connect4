"""Pelin rakenne (rivit ja sarakkeet)"""
RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
SADE = int(NELION_KOKO/2 - 5)
IKKUNA = 4

"""Pelaaja ja tekoäly"""
PELAAJA = 0
AI = 1

"""Pelaajan kiekko, tekoälyn kiekko"""
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2
TYHJA = 0

class Nakyma:
    def __init__(self, tulos = 0):
        self.tulos  = tulos

    def _näkymä(self, näkymä, kiekko):
        vastustajan_kiekko = PELAAJAN_KIEKKO
        if kiekko == PELAAJAN_KIEKKO:
            vastustajan_kiekko == AI_KIEKKO
        
        if näkymä.count(kiekko) == 4:
            self.tulos += 100
        elif näkymä.count(kiekko) == 3 and näkymä.count(TYHJA) == 1:
            self.tulos += 5
        elif näkymä.count(kiekko) == 2 and näkymä.count(TYHJA) == 2:
            self.tulos += 2
        if näkymä.count(vastustajan_kiekko) == 3 and näkymä.count(TYHJA) == 1:
            self.tulos -= 4
        return self.tulos