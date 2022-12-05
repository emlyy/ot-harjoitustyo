```mermaid
 classDiagram
      ui --> Sprites
      class Sprites{
          Ran
          Note
          Enemy
          Barrier
      }
      ui --> Actions
      class Actions{
          back
          found
          read_note
          combat
      }
      ui --> CurrentDecision
      CurrentDecision --> CurrentText
      ui --> CurrentText
      sprites --> CurrentDecision
      CurrentDecision --> Actions
      Actions --> CurrentText
```
![game loop and movement](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Game%20Loop%20and%20Movement.png)

![enemy collision](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Enemy%20collision(3).png)
