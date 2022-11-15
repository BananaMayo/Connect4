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