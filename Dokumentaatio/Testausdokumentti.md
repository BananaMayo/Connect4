## Testausdokumentti

### Yksikkötestauksen kattavuusraportti. (Unittest)
Linkki Codecovin testikattavuuksiin löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4)

![image](https://user-images.githubusercontent.com/101586122/204014432-36f8f11a-217c-4f33-b3f9-4c03b43d7fac.png)


![image](https://user-images.githubusercontent.com/101586122/204014254-47e7b459-4a10-4242-8d3e-653aae9e22ee.png)


### Mitä on testattu, miten tämä tehtiin?

#### Unit testing
* <ins> **src/luokka_nakyma.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_nakyma.py)
  - Tämä luokka käy läpi siirrot ja antaa pisteitä riippuen siirrosta. Esimerkiksi jos
asetetaan kiekko niin, että syntyy kaksi saman väristä kiekkoa peräkkäin, niin luokka lisää 2
pistettä tulokseen, kolme peräkkäistä +5 etc.
  - Luokassa testattiin pistetyksien toimivuus, eli oikea määrä kiekkoja peräkkäin lisää oikean määrän pisteitä tulokseen. Tämä saatiin testattua suhteellisen hyvin.

* <ins> **src/pelin_alustukset** </ins>
  - Tämän tiedoston testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/pelin_alustukset.py)
  - Tiedosto sisältää Minimax-algoritmin, pelin alustukseen kuuluvat osat ja kiekon sijoittamiseen liittyvän luokan.
  - Luokkaa MiniMax on testattu ja sen testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/minimax_test.py)
  - MiniMax luokassa on funktio joka on minimax-algoritmi, siinä on käytetty alpha-beta karsintaa. Algoritmin ensimmäistä osaa on testattu, ja tarkistettu
että se antaa oikean arvon mikäli tekoäly (AI) voittaa tai sitten häviää.

* <ins> **src/luokka_tulos** </ins>
  - tulossa...

### Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
--
### Miten testit voidaan toistaa?
--
### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
--
