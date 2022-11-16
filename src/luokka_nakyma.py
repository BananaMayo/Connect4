# Pelaajan kiekko, tekoälyn kiekko
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2
TYHJA = 0

class Nakyma:
    #pylint: disable=no-member
    def nakyma_(näkymä, kiekko):
        tulos = 0
        vastustajan_kiekko = PELAAJAN_KIEKKO
        if kiekko == PELAAJAN_KIEKKO:
            vastustajan_kiekko == AI_KIEKKO

        if näkymä.count(kiekko) == 4:
            tulos += 100
        elif näkymä.count(kiekko) == 3 and näkymä.count(TYHJA) == 1:
            tulos += 5
        elif näkymä.count(kiekko) == 2 and näkymä.count(TYHJA) == 2:
            tulos += 2
        if näkymä.count(vastustajan_kiekko) == 3 and näkymä.count(TYHJA) == 1:
            tulos -= 4
        return tulos
