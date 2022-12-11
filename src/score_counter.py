class ScoreCounter:
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
