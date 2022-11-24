import pygame
from sprites.ran import Ran
from sprites.background import Background
from sprites.barrier import Barrier
from config import *


class CaveGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        
        self.start = True
        self.running = False
        self.sc = True
        self.can_move = True

        self.font = pygame.font.SysFont("cmr10", 50)
        pygame.display.set_caption("Dungeon of Memories")
        

    def sprites(self):
        # for making the sprites when game starts, first room
        self.player = Ran(self, SPAWN_X,SPAWN_Y, RAN_IMAGE)
        self.bg = Background(0,0,BG_IMAGE)
        self.all_sprites.add(self.bg)
        self.all_sprites.add(self.player)
        
        for i in barriers_list:
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
    
    def text(self, text, x, y):
        t = self.font.render(text, True, WHITE)
        self.screen.blit(t, (x,y))

    def starting_screen(self):
        self.text("THIS IS THE STARTING SCREEN",30,30)
        self.text("use wasd to move Ran", 200, 300)
        self.text("press SPACE to start", 200, 400)
        self.text("you can restart any time by pressing esc", 200, 500)
        pygame.display.flip()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        # self.barriers.draw(self.screen) ## only to see the barriers
        pygame.display.update()
        self.clock.tick(60)