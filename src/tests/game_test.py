import unittest
import pygame
from sprites.ran import Ran
from sprites.note import Note
from current_decision import CurrentDecision
from actions import Actions
from current_text import CurrentText

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        self.start = True
        self.running = False
        self.start_screen = True
        self.can_move = True
        self.decisions = False
        self.next = False
        self.actions = False
        self.water = False
        self.weapon = False

        self.font1 = pygame.font.SysFont("cmr10", 50)
        self.font2 = pygame.font.SysFont("cmr10", 28)

    def restart(self):
        pass

    def update_text(self, which_text, phrase):
        which_text.update(phrase)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.player = Ran(self.game, 300, 300, "src/images/ran-1.png")
        self.game.note = Note(self.game, 500, 300, "src/images/star.png")
        self.game.text_decisions = CurrentDecision()
        self.game.text_actions = Actions()
        self.game.current_text1 = CurrentText()
        self.game.decision1 = CurrentText()
        self.game.decision2 = CurrentText()

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

    def test_cannot_move_when_note_found(self):
        self.game.player.rect.x = 500
        self.game.note.collision()
        self.assertEqual(self.game.can_move, False)


## figure a way to do this right when testing collision with walls
    #def test_ran_spawns_correctly(self):
        #self.assertEqual(self.game.player.rect.x , self.game.spawn_x)
        #self.assertEqual(self.game.player.rect.y , self.game.spawn_y)

    #def test_ran_moves_left(self):
        #self.player.c_x -= RAN_SPEED
        #x = self.player.rect.x
        #self.player.update()
        #self.assertEqual(self.player.rect.x, x - RAN_SPEED)
        
    #def test_ran_moves_right(self):
        #self.game.player.c_x += self.game.player.speed
        #x = self.game.player.rect.x
        #self.game.player.update()
        #self.assertEqual(self.game.player.rect.x, x + self.game.player.speed)

    #def test_ran_moves_up(self):
        #self.game.player.c_y -= self.game.player.speed
        #x = self.game.player.rect.y
        #self.game.player.update()
        #self.assertEqual(self.game.player.rect.y, x - self.game.player.speed)

    #def test_ran_moves_down(self):
        #self.game.player.c_y += self.game.player.speed
        #x = self.game.player.rect.y
        #self.game.player.update()
        #self.assertEqual(self.game.player.rect.y, x + self.game.player.speed)
