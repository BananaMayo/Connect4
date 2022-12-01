import unittest
#from pelipohja import pe

#Tämän luokan testaaminen ei oikein onnistu
#koska luokan importtaaminen käynnistää pygamen
#joka ei toimi CI-pipelinessä
class TestPelipohja(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_pelipohja(self):
        pass