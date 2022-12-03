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

