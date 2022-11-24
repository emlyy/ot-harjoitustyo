import pygame
from sprites.ran import Ran
from sprites.background import Background
from config import *


class CaveGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        
        self.start = True
        self.running = True
        

    def sprites(self):
        # for making the sprites when game starts, first room
        self.player = Ran(SPAWN_X,SPAWN_Y, RAN_IMAGE)
        self.bg = Background(0,0,BG_IMAGE)
        self.all_sprites.add(self.bg)
        self.all_sprites.add(self.player)
        
    def restart(self):
        pass

    def starting_screen(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
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

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)