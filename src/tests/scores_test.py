import unittest
from services.score_counter import ScoreCounter
from repository.scores import Data

class TestScoreCounter(unittest.TestCase):
    def setUp(self):
        self.scores = ScoreCounter()
        self.scores.set_name("emly")
        self.scores.add_to_score(50)
        self.scores.add_knowledge_points(1)

    def test_score_reset(self):
        self.scores.reset_scores()
        self.assertEqual(self.scores.score, 0)
        self.assertEqual(self.scores.knowledge, 1)

    def test_returns_score(self):
        self.scores.add_knowledge_points(1)
        self.scores.add_to_score(50)
        self.assertEqual(self.scores.count_total_score(), 300)

class TestScores(unittest.TestCase):
    def setUp(self):
        self.scores = Data()
        self.scores.add_scores("emly", 1400)
        

    def test_reading_scores(self):
        self.assertEqual(self.scores.read_top_scores()[0],("emly",1400))
