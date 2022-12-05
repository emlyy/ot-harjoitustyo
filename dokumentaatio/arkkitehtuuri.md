```mermaid
 classDiagram
      ui --> sprites 
      ui --> Actions
      class Actions{
          back
      }
      ui --> CurrentDecision
      CurrentDecision --> CurrentText
      ui --> CurrentText
      sprites --> combat
      sprites --> CurrentDecision
      CurrentDecision --> Actions
      Actions --> CurrentText
      combat --> CurrentDecision
```
![game loop and movement](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Game%20Loop%20and%20Movement.png)

![enemy collision](https://github.com/emlyy/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Enemy%20collision(3).png)
