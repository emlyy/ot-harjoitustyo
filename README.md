# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio
[vaatimusmäärittely](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[changelog](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[käytetyistä kuvista](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/lainatut_kuvat.md)


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
