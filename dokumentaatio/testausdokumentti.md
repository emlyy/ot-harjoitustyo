# Testausdokumentti
## Integraatio- ja yksikkötestaus
### Sovelluslogiikka
[TestCurrents](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/tests/currents_test.py)-testiluokalla testataan `CurrentDecision`- ja `CurrentText`-luokkia.

`Sprites`-luokkien testaamisesta vastaa [TestSprites](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/tests/sprites_test.py)-luokka.
[TestActions](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/tests/actions_test.py)-luokka testaa `Actions`-luokkaa. `Sprites` ja `Actions`-luokkien testeissä on `Game`-luokan tilalla käytössä `FakeGame`-luokka.

### Scores
[TestScoreCounter](https://github.com/emlyy/ot-harjoitustyo/blob/master/src/tests/scores_test.py)-luokka testaa `Data`- ja `ScoreCounter`-luokkia. Testeissä käytetään testitietokantaa, jonka tiedoston nimi on konfiguroitu .env.test-tiedostoon.

### Testauskattavuus
Testauksen haarautumakattavuus on 89%. Kattavuusraportissa ei oteta huomioon käyttöliittymää.
`Background` ja `TextBox` spritejä ei testattu, sillä se ei olisi ollut mielekästä. Testaamatta jäi myös se, että mitkä vaihtoehdot on boss fightessä riippuen siitä mitä esineitä on kerrännyt, poislukien tilanne jossa ei ole kerännyt yhtään esinettä.

## Manuaalinen testaus
Kaikkia [määrittelydokumentissa](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) kuvattuja toiminnallisuuksia on testattu manuaalisesti linux ympäristössä. Sovellus on ladattu ja käynnistetty [käyttöohjeen](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaisesti.

## Sovellukseen jääneet laatuongelmat
* Punainen valinta laatikko ilmestyy aina siihen kohtaan, kumpi vaihtoehto on valittu viimeksi.
