import sqlite3
from config import SCORE_FILE

class Data:
    """Connection to the database.
    """
    def __init__(self):
        self.file = sqlite3.connect(SCORE_FILE)

    def read_top_scores(self):
        """Reads scores from the database.

        Returns:
            list: with all the names and their score in decending order as a tuple (name, score)
        """
        scores = self.file.execute("SELECT name, score FROM Scores ORDER BY score DESC").fetchall()
        return scores

    def add_scores(self, name, score):
        """Adds the latest score into the database.

        Args:
            name (str): name that user has inputed in starting screen.
            score (int): the score they got.
        """
        try:
            self.file.execute("CREATE TABLE Scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
        except:
            pass
        self.file.execute("INSERT INTO Scores (name, score) VALUES (?, ?)", [name,score])
        self.file.commit()
