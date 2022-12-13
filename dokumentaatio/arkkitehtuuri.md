### Arkkitehtuurikuvaus

## Rakenne
Pakkaus ui sisältää käyttölittymän koodin. Pakkaukset services ja sprites sisältävät sovelluslogiikasta vastaavan koodin. Pakkaus repository sisältää koodin, joka vastaa pysyväistallennuksesta tietokantaan.

```mermaid
 classDiagram
      ui --> services
      ui --> sprites
      services --> repository
      sprites --> services
```

## Käyttöliittymä
Käyttöliittymä sisältää:
 
* aloitusnäyttö
 
* pelinäkymä
  - kolme eri tasoa
  - oveworld-näkymä ylhäällä
  - tekstilaatikko alhaalla
  
* lopetusnäyttö
 
 ## Sovelluslogiikka
Sovelluslogiikan suorittamisesta vastaa pakkauksessa services olevat luokat; spritet, Actions, CurrentDecision, CurrentText ja ScoreCounter.
Sprite oliot vastaavat eri esineisiin ja pelihahmoon liittyvistä toiminnallisuuksista. Actions-luokka vastaa CurrentDecision ja CurrentText luokkien kanssa tekstitapahtumiin liittyvistä toiminnallisuuksista. ScoreCounter vastaa tulokseen liittyvästä toiminnallisuudesta.

 Pakkaus/luokkakaavio, joka kuvaa luokkien suhdetta:
```mermaid
 classDiagram
      ui --> Sprites
      class Sprites{
          Ran
          Item
          Enemy
          Barrier
          Door
      }
      ui --> Actions
      class Actions{
          back
          found
          lines
          combat
          boss_fight
      }
      ui --> CurrentDecision
      CurrentDecision --> CurrentText
      ui --> CurrentText
      Sprites --> CurrentDecision
      Actions --> CurrentDecision
      Actions --> CurrentText
      ui --> ScoreCounter
      ScoreCounter --> repository
```

## Toiminnallisuus
![game loop and movement](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Game%20Loop%20and%20Movement.png)
