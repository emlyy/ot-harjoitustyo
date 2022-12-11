import sqlite3
from config import SCORE_FILE

class Data:
    def __init__(self):
        self.file = sqlite3.connect(SCORE_FILE)

    def read_top_scores(self):
        scores = self.file.execute("SELECT name, score FROM Scores ORDER BY score DESC").fetchall()
        return scores

    def add_scores(self, name, score):
        try:
            self.file.execute("CREATE TABLE Scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
        except:
            pass
        self.file.execute("INSERT INTO Scores (name, score) VALUES (?, ?)", [name,score])
        self.file.commit()
