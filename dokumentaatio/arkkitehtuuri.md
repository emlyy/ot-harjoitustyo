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
      Sprites --> combat
      CurrentDecision --> Actions
      Actions --> CurrentText
      
```

