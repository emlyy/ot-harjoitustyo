# Käyttöohje
## Käynnistys
1. Lataa ensin viimeisimmän releasen lähdekoodi.
2. Asenna riippuvuudet komennolla:
```
poetry install
```
3. Käynnistä ohjelma komennolla:
```
poetry run invoke start
```

## Pelin aloittaminen

Peli käynnistyy aloitusnäyttönäkymään.


![aloitus näyttö](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/start.png)

Ennen pelin aloittamista kirjoitetaan nimi.

![nimen kirjoittaminen](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/name_input.png)

Kun painetaan enter-näppäintä, peli aloitetaan.



## Pelaaminen

Pelin näkymä näyttää seruaavalta:


![pelin näkymä](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/game_view.png)


### Perus toiminnat

Hahmoa liikutetaan wasd-näppäimillä.


![move](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/images/controls.png)



Tekstivaihtoehtoa vaihdetaan nuolinäppäimillä.


![toggle](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/images/controls-2.png)



Valitaan vaihtoehto / Luetaan seuraava teksti space-näppäimellä. 


![select](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/images/controls-5.png)



Peli aloitetaan uusiksi painamalla esc-näppäimtä.


![restart](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/images/controls-3.png)



Peli suljetaan painamalla raksia.


![quit](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/quit.png)



## Tapahtumat

Jos törmää esineeseen tai viholliseen, hahmoa ei voi liikuttaa.

![itemeihin törmäys](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/collision_item.png)![viholliseen törmäys](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/combat.png)

### Tekstitapahtuman valinta

Tekstitaphtumissa on aina kaksi valintaa, joista valitaan toinen.


![teksti valinta](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/toggle_text1.png)


Punainen laatikko merkitsee, kumpi vaihtoehdoista on valittuna. Valintaa vaihdetaan nuolinäppäimillä.


![tekstivalinta 2](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/toggle_text2.png)


Lopullinen valinta tehdään painamalla space-näppäintä. Kun näytöllä on tekstiä, seuraava teksti ilmestyy aina, kun painaa space-näppäintä.


## Pelin läpäisy

Taso päättyy aina oveen.


![doors](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/doors.png)


Kun peli on läpäisty, voit nähdä oman tuloksen ja tulostaulun loppunäkymässä.


![scoreboard](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/scoreboard.png)

## Kertaus toiminnoista


![controls](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/all_controls.png)
