# Ohjelmistotekniikka, harjoitustyö
## Dungeon of Memories
Dungeon of Memories on yksinkertainen roolipeli. Käyttäjän ohjaama hahmo Ran on jumissa luolassa ja hänen pitää selvitä ulos. Matkalla voi löytää erilaisia vihjeitä ja esineitä, jotka voivat auttaa pelin läpäisemistä. Vihjeistä rakentuu myös hieman hahmon ja pelin tarinaa. Luolassa tulee vastaan woodgrem-hirviöitä. Jos törmää hirviöön, pitää taistella sitä vastaan. Käyttäjä pystyy valitsemaan eri teksti vaihtoehdoista, mitä haluaa hahmon tekevän taisteluissa.

## Releases
[release 1](https://github.com/emlyy/ot-harjoitustyo/releases/tag/viikko5)

[release 2](https://github.com/emlyy/ot-harjoitustyo/releases/tag/viikko6)

[release 3 / loppupalautus](https://github.com/emlyy/ot-harjoitustyo/releases/tag/loppupalautus)

## Dokumentaatio
[vaatimusmäärittely](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[käyttöohje](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[testausdokumentti](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

[käytetyistä kuvista](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/lainatut_kuvat.md)


## Asennus
Asenna riippuvudet komennolla:
```
poetry install
```


## Komentorivitoiminnot
Ohjelma käynnistyy komennolla:
```
poetry run invoke start
```
Testikattavuus raportti generoituu htmlcov-hakemistoon komennolla:
```
poetry run invoke coverage-report
```
Testit komennolla:
```
poetry run invoke test
```
Pylint:
```
poetry run invoke lint
```
