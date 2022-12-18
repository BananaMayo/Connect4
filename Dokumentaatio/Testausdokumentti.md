## Testausdokumentti

### Yksikkötestauksen kattavuusraportti. (Unittest)
Linkki Codecovin testikattavuuksiin löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4)

![image](https://user-images.githubusercontent.com/101586122/206667543-ab4098ed-72fa-41bc-ab7e-9fb2155d6fc0.png)

![image](https://user-images.githubusercontent.com/101586122/206667391-fea5efee-bfbe-4cc7-bb54-5d6c3124f3b1.png)


### Mitä on testattu, miten tämä tehtiin?

#### Unit testing
* <ins> **src/luokka_nakyma.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_nakyma.py)
  - Tämä luokka käy läpi siirrot ja antaa pisteitä riippuen siirrosta. Esimerkiksi jos
asetetaan kiekko niin, että syntyy kaksi saman väristä kiekkoa peräkkäin, niin luokka lisää 2
pistettä tulokseen, kolme peräkkäistä +5 etc.
  - Luokassa testattiin pistetyksien toimivuus, eli oikea määrä kiekkoja peräkkäin lisää oikean määrän pisteitä tulokseen. Tämä saatiin testattua suhteellisen hyvin.

* <ins> **src/pelin_alustukset (minima)** </ins>
  - Tämän tiedoston testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/pelin_alustukset.py)
  - Tiedosto sisältää Minimax-algoritmin, pelin alustukseen kuuluvat osat ja kiekon sijoittamiseen liittyvän luokan.
  - Funktiota minimax on testattu ja sen testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/minimax_test.py)
  - minimax-funktio on minimax-algoritmi jossa on käytetty alpha-beta karsintaa. Algoritmia on testattu, ja tarkistettu
että se antaa oikean arvon mikäli tekoäly (AI) voittaa tai sitten häviää. On myös testattu sijoituksen oletettu sijainti kun pelilauta näyttää tietyltä tavalta, eli mille sarakkeelle tekoäly sijoittaa ja paljonko pisteitä kyseisestä sijoituksesta saa.

* <ins> **src/pelin_alustukset.py (PelinAlustukset)** </ins>
  - Tämän tiedoston testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/pelin_alustukset.py)
  - Luokkaa PelinAlustukset on tarkistettu siltä osin että kiekon sijoitus onnistuu ja että seuraava avoin rivi antaa oikean avoimen rivin.
  - Luokan testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/pelin_alustukset_test.py)

* <ins> **src/luokka_tulos.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_tulos.py)
  - Tätä luokkaa on testattu numpyn luodulla pelilaudalla ja tarkistettu että tyhjällä pelilaudalla tulostuu tulokseksi 0 ja 
pelilaudalla jossa on kiekkoja tulostuu jokin tietty tulos.
  - Luokan testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/tulos_test.py)

* <ins> **src/luokka_ratkaiseva_sijotus.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_ratkaiseva_sijotus.py)
  - Tämä luokka analysoi siirtoja pelilaudalla ja havaitsee mikäli pelaaja tai tekoäly on sijoittanut niin sanotun "ratkaisevan sijotuksen", ts. kiekko on sijotettu niin että peilaudalle muodostuu neljän suora, saman värisistä kiekoista. Kun niin on tapahtunut, palautaa luokka arvon **True**.
  - Luokkaa on testattu ja sen testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/ratkaiseva_sijotus_test.py)
  - Testissä testataan manuaalisesti tehdyllä pelilaudalla että erilaiset neljän suorat tuottavat **True**-arvon.

* <ins> **src/pelipohja.py** </ins>
  - Tätä luokkaa en ole tähän mennessä onnistunut testamaan niin että se menisi CI-pipelinessä läpi pushattuani testin Githubiin. Tämä johtuu siitä
 että tiedostossa on käytetty 'pygame.init()' (ilman tätä, luokka Pelaa ei toimi) joka testattaessa käynnistää jostain syystä Pygamen. En tiedä onko CI-pipelineen edes mahdollista asentaa riippuvuus jonka avulla se pystyisi testamaan Pygamen. Taidan sen takia laittaa 'pelipohja.py'-tiedoston .coveragerc tiedostoon niin että se ei laske sitä mukaan testaukseen, sillä se laskee testikattavuutta sen verran paljon.
 

#### Manuaalinen testaus
##### Tässä stestattu kauanko tekoälyllä kestää asettaa kiekko pelilaudalle, ts. kuinka nopea MiniMax-algoritmi on:
| **TESTI 1**|Monesko kiekko | AI (Minimax) | Aika| **TESTI 2**|Monesko kiekko | AI (Minimax) | Aika |
|---|----|-----|-------------|--- |----|-----|-------------|
| | 1 | AI | 0.002861 ms|    | 1 | AI | 0.004053 ms|
| | 2 | AI |  0.002623 ms |  | 2 | AI | 0.002384 ms |
| | 3 | AI | 0.003099 ms |   | 3 | AI | 0.003099 ms |
| | 4 | AI | 0.003099 ms |   | 4 | AI |  0.004292 ms |
| | 5 | AI | 0.003099 ms |   | 5 | AI | 0.003576 ms |
| | 6 | AI | 0.003099 ms |   | 6 | AI | 0.003815 ms |
| | 7 | AI | 0.003099 ms |   | 7 | AI |  0.002861 ms |
| | 8 | AI | 0.003338 ms |   | 8 | AI | 0.002623 ms |
| | 9 | AI | 0.003099 ms |   | 9 | AI | 0.003576 ms |
| | 10 | AI | 0.003099 ms |  | 10 | AI | 0.003576 ms |
| | 11 | AI | 0.003576 ms |  | 11 | AI | 0.00453 ms |
| | 12 | AI | 0.003338 ms |  | 12 | AI | 0.004053 ms |
| | 13 | AI | 0.002623 ms |  | | | *Pelaaja voitti* |
| | 14 | AI | 0.002861 ms |  | | | |
| | 15 | AI | 0.003338 ms |  | | | |
| | 16 | AI | 0.002146 ms |  | | | |
| | 17 | AI | 0.002623 ms |  | | | |
| |  |  | *Pelaaja voitti* |   | | | |



### Minkälaisilla syötteillä testaus tehtiin?
- Testauksessa on suurimmaksi osaksi käytetty syötteenä kiekkoa, joka on numero (1=Pelaajan, 2=Tekoälyn), sekä pelilautaa joka muodostuu listasta jonka 
sisällä on rivien verran listoja joiden sisällä sarakkeiden verran numeroita.

Numpy versio näyttää tältä:

[[0. 0. 0. 0. 0. 0. 0.]

 [0. 0. 0. 0. 0. 0. 0.]
 
 [0. 0. 0. 0. 0. 0. 0.]
 
 [0. 0. 0. 0. 0. 0. 0.]
 
 [0. 0. 0. 0. 0. 0. 0.]
 
 [0. 0. 0. 0. 0. 0. 0.]]
 
 Testauksessa lauta näyttää tältä:
 
 [[0, 0, 0, 0, 0, 0, 0,],
 
 [0, 0, 0, 0, 0, 0, 0,],
 
 [0, 0, 0, 0, 0, 0, 0,],
 
 [0, 0, 0, 0, 0, 0, 0,],
 
 [0, 0, 0, 0, 0, 0, 0,],
 
 [0, 0, 0, 0, 0, 0, 0,]]
 
 Erona siis pisteet ja pilkut.
