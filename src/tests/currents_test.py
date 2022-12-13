import unittest
from ui.game import Game

class TestCurrents(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_text_decisions_works(self):
        action1 = "an action"
        action2 = "another action"
        self.game.text_decisions.update_actions(action1, action2)
        self.game.text_decisions.update("cord_y2")
        self.assertEqual(str(self.game.text_decisions) , action1)
        self.game.text_decisions.update("cord_y3")
        self.assertEqual(str(self.game.text_decisions) , action2)

    def test_updating_current_text(self):
        self.game.current_text1.update("this is the text")
        self.assertEqual(str(self.game.current_text1) , "this is the text")
