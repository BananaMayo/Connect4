## Käyttöohje

#### Miten ohjelma suoritetaan, miten eri toiminnallisuuksia käytetään
* Ensiksi kloonataan (git clone) tai ladataan koodin tiedostot omalle koneelle. Sitten siirrytään koneellaan kyseiseen kansioon. Seuraavaksi suoritetaan komento 'poetry install' kansion sisällä. Poetryn avulla voidaan suorittaa pelin käynnistys, testaus (pytest) sekä koodin laadun testaus (pylint). Ladattua poetryn siirrytään sen virtuaaliympäristöön komennolla 'poetry shell'. Päästyään virtaaliympäristöön sekä katsottuaan että sijaitsee projektin juurihakemistossa voidaan käynnistää peli, antammalla komento 'python3 src/main.py'. Jos haluaa testata pelin koodia, täytyy suorittaa komento 'pytest' tai 'pytest src/'. Mikäli haluaa käyttää pylint:ia täytyy suorittaa komento 'pylint src/'.

* Pelatessa käytetään pelkästään hiirtä. Painamalla hiiren vasenta painiketta pudotetaan kiekko pelilaudalle siihen kohtaan mihin hiiren kursori osoittaa.

```
Lyhyempi ohje:
    - Koodin lataus / git clone
    - Siirtyminen ladattuun kansioon
    - Suorita 'poetry install'
    - Virtuaaliympäristö: 'poetry shell'
    - Suorita 'python3 src/main.py'  (käynnistää pelin, ei vaadi virtuaaliympäristöä)
    - Testaus: 'pytest' tai 'pytest src/' (vaatii virtuaaliympärstön)
    - Laadun testaus: 'pylint src/' (vaatii virtuaaliympäristö)
    - Lopeteltaessa: komento exit (poistuu virtuaaliympäristöstä)
```
