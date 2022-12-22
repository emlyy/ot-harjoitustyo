import pygame
from services.current_text import CurrentText
from services.actions import Actions
from services.current_decision import CurrentDecision
from services.score_counter import ScoreCounter
from config import SCREEN_SIZE, WHITE, T_CORDS_X, T_CORDS_Y1, T_CORDS_Y2, T_CORDS_Y3, BG_COLOR

class Game:
    """Performs the game loop.

    Attributes:
        all_sprites: Sprite group for the sprites that will be updated and
            drawn always.
        barriers: Sprite group for barriers. Will be updated but not drawn.
        box: Group with one sprite (d_box). Drawn and updated only when
            decisions are made.
        enemies: Enemies that will be updated.
        see_enemies: Enemies that are drawn.
        items: Items that are drawn.
        doors: Group with one sprite (door). Only updated.

        running: While True game loop is run.
        room: Integer indicating which room is player is currently in.
        can_move: Boolean that while True allows player movement.
        decisions: Boolean indicating whether decision making is going.
        actions: Boolean indicating whether an action is being performed.
        next: Boolean indicating if user presses space to see the next text.

        water: Boolean indicating whether user decided to pick up the water bucket.
        weapon: Boolean indicating wheter user decided to pick up a weapon.

        font1: Bigger font.
        font2: Normal font.

        current_text1 = Text displayed at the top of the text box.
        decision1 = Text displayed in the middle of the text box.
        decision2 = Text displayed at the bottom of the text box.

        text_actions: Game's actions entity. Performs the current action.
        text_decisions: Game's deccision entity. Monitors the current decisions.

        score: Game's score counter entity. Keeps count of player's score.
    """    
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
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
        pygame.display.set_caption("Dungeon of Memories")

        self.current_text1 = CurrentText()
        self.decision1 = CurrentText()
        self.decision2 = CurrentText()

        self.text_actions = Actions()
        self.text_decisions = CurrentDecision()

        self.score = ScoreCounter()

    def text(self, text, font, x_pos, y_pos):
        """Draws the text on screen.

        Args:
            text (str): The text we want to display.
            font (font): The font we want to use.
            x_pos (int): X cordinate of the text.
            y_pos (int): Y cordinate of the text.
        """        
        the_text = font.render(text, True, WHITE)
        self.screen.blit(the_text, (x_pos,y_pos))

    def update_text(self, which_text, phrase):
        """Updates the specified text entity.

        Args:
            which_text (CurrentText): One of the three; current_text1, decisions1
                or decisions2
            phrase (str): The updated text.
        """        
        which_text.update(phrase)

    def speaker(self):
        self.text(str(self.current_text1), self.font2, T_CORDS_X, T_CORDS_Y1)
        self.text(str(self.decision1), self.font2, T_CORDS_X, T_CORDS_Y2)
        self.text(str(self.decision2), self.font2, T_CORDS_X, T_CORDS_Y3)

    def draw(self):
        """Draws all the sprites and text on screen.
        """        
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        self.items.draw(self.screen)
        self.speaker()
        if self.decisions is True:
            self.box.draw(self.screen)
        self.see_enemies.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)
