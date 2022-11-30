### Ohjelman yleisrakenne
Tässä kuva ohjelman yleisrakenteesta:
![image](https://user-images.githubusercontent.com/101586122/204743829-0cd8353d-3070-44f2-9911-d0522be750c2.png)
 

### Aika- ja tilavaativuuksista
Connect 4 on peli jossa on 6 riviä ja 7 saraketta, joka tekee yhteensä 42 kiekkoa (21 per pelaaja) ja 4 531 985 219 092 erilaista sijotusta. Seuraavassa on kuva joka näyttää esimerkin miltä pelipuu voisi näyttää. Jokaisen kerroksen lehdissä on seitsemän solmua (0-6), sen takia että sarakkeita on 7 joka tarkoittaa että pelin alkuvaiheissa on mahdollista sijoittaa 7 eri sarakkeelle. Pelin loppuvaiheessa tilanne voi näyttää erilaiselta, esimerkiksi vain kaksi saraketta on enää käytössä. Alla olevassa kuvassa on siis havainnollistettu miltä polku pelin lopetustilaan voisi näyttää.

![image](https://user-images.githubusercontent.com/101586122/204755578-27d0e0dc-dc1d-4b6c-9eee-aa76753460cc.png) [Lähde:https://towardsdatascience.com]

Pelin tilavaativuuden keskiarvo on noin 4.5⋅10^12 (=4,500,000,000,000) erilaista sijotusta, ja pelipuun vaativuus n. 10^21 (=1,000,000,000,000,000,000,000). Pelin tilavaativuudessa on yhteensä 42 kerrosta (plies). Seuraavassa on lista tilavaativuudesta jossa näkyy miten sijoitusten määrä kasvaa kerrosten kasvaessa.

| Kerrokset | Lehten solmut | Sijotusten määrä ('State-Space Complexity') |
|---|----|---|
| 0 | AI | 
|1 | 7 | AI | 
|2 | 49 | AI | 
|3 |  238 | AI | 
|4 | 1 120 | AI | 
|5 | 4 263 | AI | 
|6 | 16 422 | AI | 
|7 | 53 955 | AI | 
|8 | 181 597 | AI | 
|9 | 534 085  | AI |
|10| 1602 480 | AI |
|11|  | AI |
|12 | | |

*keskeneräinen*

Mitattu aika: kuinka nopeasti minimax-algoritmi (alpha-beta karsinnalla) sijottaa kiekon pelilaudalle
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

### Lähteet
* https://app.diagrams.net/
* https://www.gamesver.com/is-connect-4-a-solved-game-what-does-that-even-mean/
