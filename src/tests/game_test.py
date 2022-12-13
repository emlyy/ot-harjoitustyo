import unittest
import pygame
from sprites.ran import Ran
from sprites.note import Item
from sprites.barrier import Barrier
from sprites.enemy import Enemy
from services.current_decision import CurrentDecision
from services.actions import Actions
from services.current_text import CurrentText
from config import BARRIERS_LIST

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.see_enemies = pygame.sprite.Group()
        self.see_enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.doors = pygame.sprite.GroupSingle()
        self.start = True
        self.running = False
        self.start_screen = True
        self.second_room = False
        self.third_room = False
        self.room = 1
        self.can_move = True
        self.decisions = False
        self.next = False
        self.actions = False
        self.water = False
        self.weapon = False
        self.combat = False

        self.font1 = pygame.font.SysFont("cmr10", 50)
        self.font2 = pygame.font.SysFont("cmr10", 28)

        self.text_decisions = CurrentDecision()
        self.text_actions = Actions()
        self.current_text1 = CurrentText()
        self.decision1 = CurrentText()
        self.decision2 = CurrentText()  

    def sprites_setter(self):
        for i in BARRIERS_LIST:
            self.barriers.add(Barrier(i[0],i[1],i[2],i[3]))

    def restart(self):
        pass

    def update_text(self, which_text, phrase):
        which_text.update(phrase)

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

class TestSprites(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.player = Ran(self.game, 300, 300, "src/images/ran-1.png")
        self.game.note = Item(self.game, 500, 300, "src/images/star.png", "read_note", "back", "NOTE_FOUND", "YES", "NO")
        self.game.enemy = Enemy(self.game, 780, 270, "src/images/woodgrem-2.2.png", "normal")
        self.game.enemies.add(self.game.enemy)

    def test_cannot_move_when_note_found(self):
        self.game.player.rect.x = 500
        self.game.note.update()
        self.assertEqual(self.game.can_move, False)

    def test_cannot_move_through_barriers(self):
        self.game.sprites_setter()
        self.game.player.rect.x = 21
        self.game.player.rect.y = 230
        self.game.player.c_x -= 3
        self.game.player.c_y += 3
        if self.game.can_move is True:
            self.game.player.rect.x += self.game.player.c_x
            self.game.player.collision("x")
            self.game.player.rect.y += self.game.player.c_y
            self.game.player.collision("y")
        self.assertEqual(self.game.player.rect.x, 20)
        self.assertEqual(self.game.player.rect.y, 230+3)

    def test_enemy_collision(self):
        self.assertEqual(self.game.combat, False)
        self.assertEqual(self.game.can_move, True)
        self.assertEqual(self.game.enemies.has(self.game.enemy), True)

        self.game.player.rect.x = 780
        self.game.player.rect.y = 275
        self.game.enemy.update()

        self.assertEqual(self.game.combat, True)
        self.assertEqual(self.game.can_move, False)
        self.assertEqual(self.game.enemies.has(self.game.enemy), False)
        self.assertEqual(self.game.see_enemies.has(self.game.enemy), True)
