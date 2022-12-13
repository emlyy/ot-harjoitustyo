import pygame
from services.current_decision import CurrentDecision
from services.actions import Actions
from services.current_text import CurrentText
from services.score_counter import ScoreCounter

class Game:
    """at the moment useless as the tests use the real Game class
    """
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

        self.text_decisions = CurrentDecision()
        self.text_actions = Actions()
        self.current_text1 = CurrentText()
        self.decision1 = CurrentText()
        self.decision2 = CurrentText()

        self.score = ScoreCounter()

    def update_text(self, which_text, phrase):
        which_text.update(phrase)
