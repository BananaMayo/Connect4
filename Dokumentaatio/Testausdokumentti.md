## Testausdokumentti

### Yksikkötestauksen kattavuusraportti. (Unittest)
Linkki Codecovin testikattavuuksiin löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4)

![image](https://user-images.githubusercontent.com/101586122/205009966-b04d8bc1-b684-4ad0-90fd-fc272f74fa7d.png)

![image](https://user-images.githubusercontent.com/101586122/205009705-0899ee8e-b33e-4020-a1a9-a78dd154a7a5.png)

### Mitä on testattu, miten tämä tehtiin?

#### Unit testing
* <ins> **src/luokka_nakyma.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_nakyma.py)
  - Tämä luokka käy läpi siirrot ja antaa pisteitä riippuen siirrosta. Esimerkiksi jos
asetetaan kiekko niin, että syntyy kaksi saman väristä kiekkoa peräkkäin, niin luokka lisää 2
pistettä tulokseen, kolme peräkkäistä +5 etc.
  - Luokassa testattiin pistetyksien toimivuus, eli oikea määrä kiekkoja peräkkäin lisää oikean määrän pisteitä tulokseen. Tämä saatiin testattua suhteellisen hyvin.

* <ins> **src/pelin_alustukset (MiniMax)** </ins>
  - Tämän tiedoston testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/pelin_alustukset.py)
  - Tiedosto sisältää Minimax-algoritmin, pelin alustukseen kuuluvat osat ja kiekon sijoittamiseen liittyvän luokan.
  - Luokkaa MiniMax on testattu ja sen testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/minimax_test.py)
  - MiniMax luokassa on funktio joka on minimax-algoritmi, siinä on käytetty alpha-beta karsintaa. Algoritmin ensimmäistä osaa on testattu, ja tarkistettu
että se antaa oikean arvon mikäli tekoäly (AI) voittaa tai sitten häviää.

* <ins> **src/pelin_alustukset.py (PelinAlustukset)** </ins>
  - Tämän tiedoston testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/pelin_alustukset.py)
  - Luokkaa PelinAlustukset on tarkistettu siltä osin että kiekon sijoitus onnistuu ja että seuraava avoin rivi antaa oikean avoimen rivin.
  - Luokan testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/pelin_alustukset_test.py)

* <ins> **src/luokka_ratkaiseva_sijotus.py** </ins>
  - Tämän luokan testikattavuus löytyy [täältä](https://app.codecov.io/gh/BananaMayo/Connect4/blob/main/src/luokka_ratkaiseva_sijotus.py)
  - Tämä luokka analysoi siirtoja pelilaudalla ja havaitsee mikäli pelaaja tai tekoäly on sijoittanut niin sanotun "ratkaisevan sijotuksen", ts. kiekko on sijotettu niin että peilaudalle muodostuu neljän suora, saman värisistä kiekoista. Kun niin on tapahtunut, palautaa luokka arvon **True**.
  - Luokkaa on testattu ja sen testitiedosto löytyy [täältä](https://github.com/BananaMayo/Connect4/blob/main/src/tests/ratkaiseva_sijotus_test.py)
  - Testissä testataan manuaalisesti tehdyllä pelilaudalla että erilaiset neljän suorat tuottavat **True**-arvon.

* <ins> **src/pelipohja.py** </ins>
  - Tätä luokkaa en ole tähän mennessä onnistunut testamaan niin että se menisi CI-pipelinessä läpi pushattuani testin Githubiin. Tämä johtuu siitä
 että tiedostossa on käytetty 'pygame.init()' (ilman tätä, luokka Pelaa ei toimi) joka testattaessa käynnistää jostain syystä Pygamen. En tiedä onko CI-pipelineen edes mahdollista asentaa riippuvuus jonka avulla se pystyisi testamaan Pygamen. Taidan sen takia laittaa 'pelipohja.py'-tiedoston .coveragerc tiedostoon niin että se ei laske sitä mukaan testaukseen, sillä se laskee testikattavuutta sen verran paljon.
 

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

### Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
    - tulossa...
