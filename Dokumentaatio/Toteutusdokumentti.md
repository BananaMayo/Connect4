### Ohjelman yleisrakenne
Tässä kuva ohjelman yleisrakenteesta:
![image](https://user-images.githubusercontent.com/101586122/204743829-0cd8353d-3070-44f2-9911-d0522be750c2.png)
 

Connect 4 on peli jossa on 6 riviä ja 7 saraketta, joka tekee yhteensä 42 kiekkoa (21 per pelaaja) ja n. 4 531 985 219 092 erilaista sijotusta. Seuraavassa on kuva joka näyttää esimerkin miltä pelipuu voisi näyttää. Solmuja on seitsemän (0-6) sen takia, että sarakkeita on 7 joka tarkoittaa että pelin alkuvaiheissa on mahdollista sijoittaa 7 eri sarakkeelle. Pelin loppuvaiheessa tilanne voi näyttää erilaiselta, esimerkiksi vain.on siis havainnollistettu miltä polku pelin lopetustilaan voisi näyttää.

![image](https://user-images.githubusercontent.com/101586122/204755578-27d0e0dc-dc1d-4b6c-9eee-aa76753460cc.png) [Lähde:https://towardsdatascience.com]


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
