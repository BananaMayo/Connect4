## Määrittelydokumentti

TKT20010 Tiralabra syksy 2022, Helsingin Yliopisto. Projektissa käytettävä kieli on **suomi**.

#### "Connect four"
Suomeksi "Neljän suora", on kahdelle henkilölle tarkoitettu lautapeli. Pelissä pelaajat pudottavat 
vuorotellen kiekkoja ("tokens") pelilautaan, koittaen saada aikaan neljän saman värisen kiekon
suora. 

Projektin tarkoituksena olisi luoda pelille AI-vastustaja, jota vastaan pystyy pelaamaan.
Toisin sanoen pelille tulisi luoda tekoäly jota vastaan ihminen pystyy pelaamaan.

### Ohjelmointikieli
* Peliä sekä algoritmia varten tulen käyttämään **Pythonia**. Osaan hieman R- ja SQL-ohjelmointikieltä
sekä HTML-merkintäkieltä.

### Algoritmit ja tietorakenteet
* Algoritmina tulen käyttämään Minimax:ia, sekä Alpha-Beta karsintaa joka vähentäisi Minimax-algoritmin
arvioimien solmujen määrää.

* Valitsen Minimax-algoritmin koska sitä käytetään yleensä päätöksenteoissa ja peliteoriassa, jossa
on tarkoitus löytää optimaalinen liike.

### Syötteet ohjelmalle
Ohjelman syöte tulee olemaan pelaajan siirrot, jossa hän valitsee mille sarakkeelle hän asettaa kiekon. Tämä
siirto tallentuu taulukkoon (pelilaudalle) josta pystyy näkemään pelitilanteen.


### Aika- ja tilavaativuudet
Aikavaativuus Minimax-algoritmilla on O(b^m) ja tilavaativuus on O(bm), missä b on laillisten siirtojen lukumäärä
kussakin pisteessä ja m on puun suurin syvyys.


### Lähteet
* https://en.wikipedia.org/wiki/Connect_Four
* https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html#algorithm
* http://www.pygame.org/docs/ref/draw.html
* https://cis.temple.edu/~vasilis/Courses/CIS603/Lectures/l7.html

