import pygame
from sprites.ran import Ran
from sprites.background import Background
from sprites.barrier import Barrier
from sprites.texts import TextBox
from sprites.note import Note
from config import *
from current_text import CurrentText
from sprites.text_lines import *
from actions import Actions
from current_decision import CurrentDecision


class CaveGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        
        self.start = True
        self.running = False
        self.sc = True
        self.can_move = True
        self.decisions = False
        self.next = False
        self.actions = False

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
        

    def sprites(self):
        # for making the sprites when game starts, first room
        self.player = Ran(self, SPAWN_X,SPAWN_Y, RAN_IMAGE)
        self.bg = Background(0,0,BG_IMAGE)
        self.note = Note(self, NOTE_X, NOTE_Y, NOTE_IMAGE)
        self.d_box = TextBox(self, (255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)
        self.box.add(self.d_box)
        self.all_sprites.add(self.bg)
        self.all_sprites.add(TextBox(self, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636))
        self.all_sprites.add(TextBox(self, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636))
        self.all_sprites.add(self.note)
        self.all_sprites.add(self.player)
        
        for i in BARRIERS_LIST:
            self.barriers.add(Barrier(i[0],i[1],i[2],i[3]))

        
        
    def restart(self):
        pass
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                
            if self.sc == True:
                self.starting_screen()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.sc = False
                        self.running = True
                        break
                continue

            if event.type == pygame.KEYDOWN:
                if self.decisions == True:
                    if event.key == pygame.K_DOWN:
                        self.d_box.update_rect(Y3)
                    if event.key == pygame.K_UP:
                        self.d_box.update_rect(Y2)
                
                if event.key == pygame.K_SPACE:
                    if self.decisions == True:
                        if self.d_box.rect.y == Y2:
                            self.text_decisions.update("y2")
                            action = str(self.text_decisions)
                            self.text_actions.update_current(action)
                            self.text_actions.act(self)
                            self.decisions = False
                            self.actions = True
                        if self.d_box.rect.y == Y3:
                            self.text_decisions.update("y3")
                            action = str(self.text_decisions)
                            self.text_actions.update_current(action)
                            self.text_actions.act(self)
                            self.decisions = False                      #decision stuff
                            self.actions = True
                    else:
                        if self.actions == True:
                            self.next = True
                            self.text_actions.act(self)
                            self.next = False

                if self.can_move == True:
                    if event.key == pygame.K_a:
                        self.player.c_x -= RAN_SPEED
                    if event.key == pygame.K_d:
                        self.player.c_x += RAN_SPEED
                    if event.key == pygame.K_s:
                        self.player.c_y += RAN_SPEED
                    if event.key == pygame.K_w:
                        self.player.c_y -= RAN_SPEED
                
                if event.key == pygame.K_ESCAPE:
                    self.restart()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.c_x = 0
                if event.key == pygame.K_d:
                    self.player.c_x = 0
                if event.key == pygame.K_s:
                    self.player.c_y = 0
                if event.key == pygame.K_w:
                    self.player.c_y = 0  
    
    def text(self, text, font, x, y):
        t = font.render(text, True, WHITE)
        self.screen.blit(t, (x,y))

    def update_text(self, id, phrase):
        id.update(phrase)
    
    def speaker(self):
        self.text(str(self.current_text1), self.font2, T_CORDS_X, T_CORDS_Y1)
        self.text(str(self.decision1), self.font2, T_CORDS_X, T_CORDS_Y2)
        self.text(str(self.decision2), self.font2, T_CORDS_X, T_CORDS_Y3)

    def starting_screen(self):
        self.text("THIS IS THE STARTING SCREEN",self.font1,30,30)
        self.text("use wasd to move", self.font1, 200, 300)
        self.text("press SPACE to start", self.font1, 200, 400)
        self.text("you can restart any time by pressing esc", self.font1, 200, 500)
        pygame.display.flip()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        self.speaker()
        if self.decisions == True:
            self.box.draw(self.screen)
        #self.barriers.draw(self.screen) ## only to see the barriers
        pygame.display.update()
        self.clock.tick(60)