# Changelog
## viikko 3
- käyttäjä näkee taustan ja pystyy liikuttamaan hahmoa
- lisätty ran-sprite, asettaa koordinaatit, lataa kuvan, sisältää update metodin, joka päivittää koordinaatit
- lisätty background-sprite, lataa kuvan, asettaa koordinaatit
- molemmat spritet kuuluu all_sprites ryhmään
- lisätty CaveGame-luokka vastaa tapahtumista, spritejen piirtämisestä ja main-loopista
- testattu, että hahmo piirretään oikeaan aloituskohtaan ja hahmo voi liikkua eri suuntiin

## viikko 4
- alustava aloitus sivu
- hahmoa ei voi liikuttaa rajojen ulkopuolelle
- käyttäjä näkee ruudun alareunassa laatikon, johon ilmestyy tekstiä.
- kun törmää ruudulla näkyvään pieneen tähteen (note), teksti kertoo, että se on kirje ja kysyy haluaako lukea sen. Käyttäjä pystyy valitsemaan nuolinäppäimillä.
- CaveGame-luokka nimetty uudelleen (Game) ja jaettu pienempiin osiin; sprites, events ja main.
- uudet luokat: CurrentDecision (vastaa tekstivalinnoista), Actions (vastaa siitä mitkä tekstit päivitetään seuraavaksi), CurrentText (päivittää ja paluattaa tällä hetkellä näkyvän tekstin)
- uudet spritet: Note (lataa kuvan, asettaa koordinaatit, tarkistaa törmäyksen pelaajan kanssa ja aloittaa törmäyksestä johtavat tehtävät), Barrier (asettaa koordinaatit rajoille), TextBox (käytetään alareunassa olevan tekstilaatikon luomiseen ja punaisen laatikon, josta näkee kumpi vaihtoehdoista on valittu sillä hetkellä)
- testattu tekstivallinnan vaihtaminen toimii oikein (CurrentDecision), tämän hetkinen teksti päivittyy oikein (CurrentText), Back-Action palauttaa tämän hetkiset tekstit tyhjiksi, hahmoa voi taas liikuttaa, kun löytää kirjeen hahmoa ei voi liikuttaa 

## viikko 5
- enemy-sprite lisätty, enemy.update vastaa törmäyksien pelaajaan kanssa tarkastamisesta
- kun törmää viholliseen näkyy eri tekstivalintoja ja kun valitsee niin valintaa vastaava teksti ilmestyy
- voi aloittaa pelin uudelleen painamalla esc
- uudet luokat: Rooms (vastaa eri huoneista, first_room pitää huolen että oikeat spritet on mukana), Restart (kutsuu tarvittavat metodit, jotta pelin voi aloittaa uudestaan, muuttaa tarvittavat muuttujat alku asentoon), SpriteSet
- testattu: hahmoa ei voi liikuttaa rajojen ukopuolelle, hirviöön törmääminen

## viikko 6
- aloitus sivulla voi kirjoittaa nimen ja peli käynnistyy enter näppäimellä
- pelin päätyttyä tallennetaan nimi ja tulos tietokantaan, ja käyttäjä voi nähdä oman tuloksen ja tulostaulun lopetus sivulla
- boss fight lisätty, tämä toteutetaan Actions luokan avulla
- uudet luokat: ending_screen (vastaa lopetusnäytöstä)
- first_room, second_room ja third_room siirretty SpriteSet-luokkaan.
- uudet spritet: Door (kun törmää taso on läpäisty ja siirrytään seuraavalle tasolle), Note sprite uudelleen nimetty; nyt Item
- Actions luokassa uusia metodeja boss_fight, first_room_actions, second_room_actions ja third_room_actions. Lisäksi metodi read_note uudelleen nimetty lines-metodiksi
- testattu kun törmää boss tyyppiseen viholliseen, door spriten toimintaa, Data ja ScoreCounter luokkia, Action luokasta testattu metodeja lines ja intro

## vikko 7
- aloitusnäytöllä näkyy kuva vihollisesta ja puhekupla, myös toiseen ja kolmanteen tasoon lisätty taustalle kuvia
- lisätty esineitä; water, sword, memory book, cheese
- boss fight; viholliset häviävät näytöltä taistelun jälkeen, itemi-vaihtoehdot nyt myös käytössä. Jos ei itemejä niin oma toiminto (teleportation).
- testattu: Actions: restartin jälkeen tekstit toimii oikein, rng-toiminta, teleportaatio toimii oikein, counter toimii oikein, tulos oikein eri toimintojen jälkeen, boss_fight, eri metodien yhteistoiminta; act, first/second/third_room_actions, lines, found, back, boss_fight,
