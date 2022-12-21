import unittest
from services.current_decision import CurrentDecision
from services.current_text import CurrentText

class TestCurrents(unittest.TestCase):
    def setUp(self):
        self.text_decisions = CurrentDecision()
        self.current_text1 = CurrentText()

    def test_text_decisions_works(self):
        action1 = "an action"
        action2 = "another action"
        self.text_decisions.update_actions(action1, action2)
        self.text_decisions.update("cord_y2")
        self.assertEqual(str(self.text_decisions) , action1)
        self.text_decisions.update("cord_y3")
        self.assertEqual(str(self.text_decisions) , action2)

    def test_updating_current_text(self):
        self.current_text1.update("this is the text")
        self.assertEqual(str(self.current_text1) , "this is the text")
