import unittest
from ui.game import Game
from ui.sprite_setter import SpriteSet
from text_lines import EAT_LIST

class TestActions(unittest.TestCase):
    def setUp(self):
        self.game = Game() 

    def test_back_action_enables_movement_and_resets_texts(self):
        self.game.current_text1.update("text1")
        self.game.decision1.update("text2")
        self.game.decision2.update("text3")
        self.game.text_actions.back(self.game)

        self.assertEqual(str(self.game.current_text1) , "")
        self.assertEqual(str(self.game.decision1) , "")
        self.assertEqual(str(self.game.decision2) , "")
        self.assertEqual(self.game.next, False)
        self.assertEqual(self.game.can_move, True)
        self.assertEqual(self.game.actions, False)
    
    def test_intro_sets_texts(self):
        self.game.text_actions.intro(self.game, "this text")
        self.assertEqual(str(self.game.current_text1) , "this text")
        self.assertEqual(str(self.game.decision1) , "")
        self.assertEqual(str(self.game.decision2) , "")

    def test_lines_sets_text(self):
        SpriteSet().sprites_setter(self.game)
        SpriteSet().second_room(self.game)
        self.game.text_actions.update_current("eat")
        for i in EAT_LIST:
            self.game.text_actions.act(self.game)
            self.game.next = True
            self.assertEqual(str(self.game.current_text1) , i)
