class ScoreCounter:
    """Keeps track of the score.

    Attributes:
        name: A string. The name that user inputs during starting screen.
        score: An integer counting the score.
        knowledge: An integer counting the collected knowledge points.
    """    
    def __init__(self):
        self.name = ""
        self.score = 0
        self.knowledge = 1

    def set_name(self, name):
        self.name = name

    def reset_scores(self):
        self.score = 0
        self.knowledge = 1

    def add_knowledge_points(self, amount):
        self.knowledge += amount

    def add_to_score(self, amount):
        self.score += amount

    def count_total_score(self):
        return self.score * self.knowledge
