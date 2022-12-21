import unittest
import pygame
from ui.sprite_setter import SpriteSet
from ui.restart import restart
from services.current_decision import CurrentDecision
from services.current_text import CurrentText
from services.actions import Actions
from services.score_counter import ScoreCounter
from text_lines import EAT_LIST, PUNCH_1, PUNCH_1A, PUNCH_2A, ROCK_1, ROCK_1B, ROCK_2B, SWORD, WATER, NOTE_1

class Game:
    def __init__(self): 
        pygame.init()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.box = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.see_enemies = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.doors = pygame.sprite.GroupSingle()

        self.running = False
        self.room = 1
        self.can_move = True
        self.decisions = False
        self.actions = False
        self.next = False

        self.water = False
        self.weapon = False

        self.font1 = pygame.font.SysFont("cmr10", 50)
        self.font2 = pygame.font.SysFont("cmr10", 28)

        self.current_text1 = CurrentText()
        self.decision1 = CurrentText()
        self.decision2 = CurrentText()

        self.text_actions = Actions()
        self.text_decisions = CurrentDecision()
        self.score = ScoreCounter()

    def update_text(self, which_text, phrase):
        which_text.update(phrase)

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

    def test_no_water_awards_no_points(self):
        self.game.text_actions.update_current("no water")
        self.game.text_actions.counter = 1
        self.game.text_actions.act(self.game)
        self.assertEqual(self.game.score.score, 0)
        self.assertEqual(self.game.score.knowledge, 1)

    def test_if_not_no_water_lines_awards_points(self):
        self.game.room = 2
        self.game.text_actions.update_current("memory book")
        self.game.text_actions.counter = 1
        self.game.text_actions.act(self.game)
        self.assertEqual(self.game.score.score, 50)
        self.assertEqual(self.game.score.knowledge, 2)

    def test_when_counter_is_equal_to_len_in_lines(self):
        self.game.room = 3
        self.game.can_move = False
        self.game.text_actions.update_current("talk")
        self.game.text_actions.act(self.game)
        self.game.text_actions.counter = 2
        self.game.text_actions.act(self.game)
        self.assertEqual(len(self.game.see_enemies), 0)
        self.assertEqual(str(self.game.current_text1) , "")
        self.assertEqual(str(self.game.decision1) , "")
        self.assertEqual(str(self.game.decision2) , "")
        self.assertEqual(self.game.can_move, True)

    def test_tp_works_when_allowed(self):
        SpriteSet().sprites_setter(self.game)
        self.game.text_actions.teleport = True
        self.game.text_actions.back(self.game)
        self.assertEqual(self.game.player.rect.x, 600)
        self.assertEqual(self.game.player.rect.y, 150)
        self.assertEqual(self.game.text_actions.teleport, False)
        self.game.player.rect.x = 400
        self.game.player.rect.y = 400
        self.game.text_actions.back(self.game)
        self.assertEqual(self.game.player.rect.x, 400)
        self.assertEqual(self.game.player.rect.y, 400)
        self.assertEqual(self.game.text_actions.teleport, False)

    def test_combat_texts_rng_0(self):
        self.game.text_actions.update_current("punch")
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , PUNCH_1)
        self.game.text_actions.rng = 0
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , PUNCH_1A)
        self.game.text_actions.act(self.game)
        self.assertEqual(str(self.game.current_text1) , PUNCH_2A)

    def test_combat_texts_rng_1(self):
        self.game.text_actions.update_current("throw_rock")
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , ROCK_1)
        self.game.text_actions.rng = 1
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , ROCK_1B)
        self.game.text_actions.act(self.game)
        self.assertEqual(str(self.game.current_text1) , ROCK_2B)

    def test_boss_fight_rng_0(self):
        SpriteSet().sprites_setter(self.game)
        SpriteSet().third_room(self.game)
        self.game.text_actions.update_current("sword")
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.game.text_actions.rng = 0
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , SWORD[1])
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , SWORD[4])
        self.game.text_actions.act(self.game)
        self.assertEqual(self.game.score.knowledge , 2)
        self.assertEqual(len(self.game.see_enemies), 0)

    def test_boss_fight_rng_1(self):
        SpriteSet().sprites_setter(self.game)
        SpriteSet().third_room(self.game)
        self.game.text_actions.update_current("water bucket")
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.game.text_actions.rng = 1
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , WATER[3])
        self.game.text_actions.act(self.game)
        self.game.next = True
        self.assertEqual(str(self.game.current_text1) , WATER[4])
        self.game.text_actions.act(self.game)
        self.assertEqual(self.game.score.knowledge , 2)
        self.assertEqual(len(self.game.see_enemies), 0)

    def test_boss_with_no_items(self):
        self.game.room = 3
        self.game.water = False
        self.game.weapon = False
        self.game.text_actions.update_current("item")
        self.game.text_actions.act(self.game)
        self.assertEqual(self.game.text_actions.current_action, "no item")

    def test_after_restart_text_is_correct(self):
        SpriteSet().sprites_setter(self.game)
        SpriteSet().third_room(self.game)
        self.game.text_actions.update_current("talk")
        self.game.text_actions.act(self.game)
        restart(self.game)
        self.game.text_actions.update_current("read_note")
        self.game.text_actions.act(self.game)
        self.assertEqual(str(self.game.current_text1), NOTE_1)
