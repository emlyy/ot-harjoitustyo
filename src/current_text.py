class CurrentText:
    """The text that will be shown on screen.

    Attributes:
        phrase: A string, the text.
    """
    def __init__(self):
        self.phrase = ""

    def update(self, phrase):
        self.phrase = phrase

    def __str__(self) -> str:
        return self.phrase
