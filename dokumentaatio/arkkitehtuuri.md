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
      CurrentDecision --> Actions
      Actions --> CurrentText
      combat --> CurrentDecision
```

