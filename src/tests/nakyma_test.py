import unittest
from luokka_nakyma import Nakyma

RIVIT = 6
SARAKKEET = 7
NELION_KOKO = 100
PELAAJAN_KIEKKO = 1
AI_KIEKKO = 2

class TestNakyma(unittest.TestCase):
    def setUp(self):
        self.PELAAJAN_KIEKKO = 1
        self.PELAAJA = 0
        self.näkymä = []
        self.kiekko = 1
        Nakyma.nakyma_(self.näkymä, self.kiekko)
    
    def test_kiekko(self):
        kiekko = PELAAJAN_KIEKKO
        näkymä = []
        testi = Nakyma.nakyma_(näkymä, kiekko)
        print(testi)
        #self.assertEqual(kiekko, AI_KIEKKO)

    def test_nakyma_count(self):
        näkymä = [1,1,1,1]
        kiekko = 1
        Nakyma.nakyma_(näkymä,kiekko)
        a = näkymä.count(kiekko)
        self.assertEqual(a, 4)

    def test_nakyma_4(self):
        näkymä = [1,1,1,1]
        kiekko = 1
        c = Nakyma.nakyma_(näkymä,kiekko)
        self.assertEqual(c, 100)

    def test_nakyma_3(self):
        näkymä = [1,1,1,0]
        kiekko = 1
        tyhja = 0
        b = Nakyma.nakyma_(näkymä, kiekko)
        self.assertEqual(b, 1)
    
    def test_nakyma_2(self):
        näkymä = [1,1,0,0]
        kiekko = 1
        d = Nakyma.nakyma_(näkymä,kiekko)
        self.assertEqual(d, 2)
