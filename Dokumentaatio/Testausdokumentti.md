## Testausdokumentti

### Yksikkötestauksen kattavuusraportti. (Unittest)
Linkki Codecovin testikattavuuksiin löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4)

![image](https://user-images.githubusercontent.com/101586122/202242600-e285e62a-d9a8-4f8c-acc7-18c7b460d346.png)

![image](https://user-images.githubusercontent.com/101586122/202242167-c86b5a68-4b00-4fe0-9363-c8c3da0a6357.png)

### Mitä on testattu, miten tämä tehtiin?

#### Unit testing
* <ins> **src/luokka_nakyma.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_nakyma.py)
  - Tämä luokka käy läpi siirrot ja antaa pisteitä riippuen siirrosta. Esimerkiksi jos
asetetaan kiekko niin, että syntyy kaksi saman väristä kiekkoa peräkkäin, niin luokka lisää 2
pistettä tulokseen, kolme peräkkäistä +5 etc.
  - Luokassa testattiin pistetyksien toimivuus, eli oikea määrä kiekkoja peräkkäin lisää oikean määrän pisteitä tulokseen. Tämä saatiin testattua suhteellisen hyvin.

* <ins> **src/luokka_tulos** </ins>
  - tulossa...

### Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?
--
### Miten testit voidaan toistaa?
--
### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
--
