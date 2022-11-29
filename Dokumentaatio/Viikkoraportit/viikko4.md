Neljännen viikon tunnit: [Tehdyt tunnit](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Ty%C3%B6tunnit.md#viikko4)

### Mitä olen tehnyt tällä viikolla?
* Tällä viikolla olen edistänyt minimax-algoritmia ja saanut sen valmiiksi
* Muokkailut luokkia sen verran että importit toimii paremmin
* Saanut pelin pelattavaksi
* Tehnyt testejä, mm. minimax-algoritmia varten
* Refaktoroinut tiedostoja jotta CI-pipeline toimisi ilman että tarvitsee käynnistää pygamea testeissä
* Mitannut aikoja pelesistä, ts. tarkistanut kauanko minimax-algoritmilla kestää asettaa kiekko pelilaudalle

### Miten ohjelma on edistynyt?
* Peli on suurimmalta osalta valmis, siinä pystyy jo pelaamaan algoritmia vastaan
* Ohjelman AI-algoritmi, minimax-algoritmi, on suurimmalta osalta valmis
* Algoritmi toimii kohtalaisen hyvin ja nopeasti, ja on myös suhteellisen vaikea vastustajana

### Mitä opin tällä viikolla / tänään?
* Opin paremmin erilaisista pylint säännöistä, mitä ne tarkoittavat ja miten niitä saa korjattua

### Mikä jäi epäselväksi tai tuottanut vaikeuksia?
* Testien teko, mutta edistyy... Varsinkin pelipohja.py:n testaaminen on hankalaa sillä pelkästään luokan importaaminen tiedostosta käynnistää 
pygamen joka ei taas mene CI-pipelinessä läpi. Tälle ongelmalle en keksi ratkaisua, ainakaan vielä.

### Mitä teen seuraavaksi?
* Seuraavaksi olisi tavoitteena saada mahdollisimman kattavat testit aikaiseksi, mm. pelipohja.py jossa 0% tällä hetkellä. Myös aikavaativuuden laskentaa
pitäisi edistää, jota en kerennyt tällä viikolla tehdä.
