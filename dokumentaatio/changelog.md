# Changelog
## viikko 3
- käyttäjä näkee taustan ja pystyy liikuttamaan hahmoa
- lisätty ran-sprite, asettaa koordinaatit, lataa kuvan, sisältää update metodin, joka päivittää koordinaatit
- lisätty background-sprite, lataa kuvan, asettaa koordinaatit
- molemmat spritet kuuluu all_sprites ryhmään
- lisätty CaveGame-luokka vastaa tapahtumista, spritejen piirtämisestä ja main-loopista
- testattu, että hahmo piirretään oikeaan aloituskohtaan ja hahmo voi liikkua eri suuntiin

## viiko 4
- alustava aloitus sivu
- hahmoa ei voi liikuttaa rajojen ulkopuolelle
- käyttäjä näkee ruudun alareunassa laatikon, johon ilmestyy tekstiä.
- kun törmää ruudulla näkyvään pieneen tähteen (note), teksti kertoo, että se on kirje ja kysyy haluaako lukea sen. Käyttäjä pystyy valitsemaan nuolinäppäimillä.
- CaveGame-luokka nimetty uudelleen (Game) ja jaettu pienempiin osiin; sprites, events ja main.
- uudet luokat: CurrentDecision (vastaa tekstivalinnoista), Actions (vastaa siitä mitkä tekstit päivitetään seuraavaksi), CurrentText (päivittää ja paluattaa tällä hetkellä näkyvän tekstin)
- uudet spritet: Note (lataa kuvan, asettaa koordinaatit, tarkistaa törmäyksen pelaajan kanssa ja aloittaa törmäyksestä johtavat tehtävät), Barrier (asettaa koordinaatit rajoille), TextBox (käytetään alareunassa olevan tekstilaatikon luomiseen ja punaisen laatikon, josta näkee kumpi vaihtoehdoista on valittu sillä hetkellä)
- testattu tekstivallinnan vaihtaminen toimii oikein (CurrentDecision), tämän hetkinen teksti päivittyy oikein (CurrentText), Back-Action palauttaa tämän hetkiset tekstit tyhjiksi, hahmoa voi taas liikuttaa, kun löytää kirjeen hahmoa ei voi liikuttaa 
