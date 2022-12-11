import pygame
from current_text import CurrentText
from actions import Actions
from current_decision import CurrentDecision
from score_counter import ScoreCounter
from config import SCREEN_SIZE, WHITE, T_CORDS_X, T_CORDS_Y1, T_CORDS_Y2, T_CORDS_Y3, BG_COLOR

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.see_enemies = pygame.sprite.Group()
        self.start = True
        self.running = False
        self.start_screen = True
        self.can_move = True
        self.decisions = False
        self.next = False
        self.actions = False
        self.water = False
        self.weapon = False
        self.combat = False

        self.font1 = pygame.font.SysFont("cmr10", 50)
        self.font2 = pygame.font.SysFont("cmr10", 28)
        pygame.display.set_caption("Dungeon of Memories")

        self.current_text1 = CurrentText()
        self.decision1 = CurrentText()
        self.decision2 = CurrentText()

        self.text_actions = Actions()
        self.text_decisions = CurrentDecision()

        self.score = ScoreCounter()

    def text(self, text, font, x_pos, y_pos):
        the_text = font.render(text, True, WHITE)
        self.screen.blit(the_text, (x_pos,y_pos))

    def update_text(self, which_text, phrase):
        which_text.update(phrase)

    def speaker(self):
        self.text(str(self.current_text1), self.font2, T_CORDS_X, T_CORDS_Y1)
        self.text(str(self.decision1), self.font2, T_CORDS_X, T_CORDS_Y2)
        self.text(str(self.decision2), self.font2, T_CORDS_X, T_CORDS_Y3)

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        self.speaker()
        if self.decisions is True:
            self.box.draw(self.screen)
        if self.combat is True:
            self.see_enemies.draw(self.screen)
        #self.barriers.draw(self.screen) ## only to see the barriers
        pygame.display.update()
        self.clock.tick(60)
