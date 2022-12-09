# Connect4
![CI](https://github.com/BananaMayo/Connect4/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/BananaMayo/Connect4/branch/main/graph/badge.svg?token=69W5G19QKL)](https://codecov.io/gh/BananaMayo/Connect4)

Kurssi: TKT20010 Tiralabra syksy 2022, Helsingin Yliopisto

Aiheena tehdä algoritmi minimaxilla joka luo AI-vastustajan pelissä "Connect Four"

Ohjelmointikieli tulee olemaan Python

## Linkit dokumentointiin
### [Määrittelydokumentti](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)
### [Testausdokumentti](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Testausdokumentti.md#testausdokumentti)
### [Toteutusdokumentti](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Toteutusdokumentti.md)
### [Työtunnit](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Ty%C3%B6tunnit.md)

### [Viikkoraportit](https://github.com/BananaMayo/Connect4/tree/main/Dokumentaatio/Viikkoraportit)
- [Viikko1](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko1.md)
- [Viikko2](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko2.md)
- [Viikko3](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko3.md)
- [Viikko4](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko4.md)
- [Viikko5](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko5.md)
- [Viikko6](https://github.com/BananaMayo/Connect4/blob/main/Dokumentaatio/Viikkoraportit/viikko6.md)

## Käyttöohje
* Lataa koodi omalle koneelle komennolla: 
``` 
$ git clone <linkki>
```
* Siirry projektin juurihakemistoon ja suorita komento:
```
$ poetry install
```
* Siirry virtuaaliympäristöön komennolla:
```
$ poetry shell
```
* Käynnistä peli komennolla:
```
$ python3 src/main.py
```
* suorita testit komennolla:
```
$ pytest src/ 
```
* tai laaduntarkistus testi komennolla:
```
$ pylint src/
```
