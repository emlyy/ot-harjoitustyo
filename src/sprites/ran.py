import pygame

class Ran(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.speed = 3

        self.image = pygame.image.load("images/ran1.png")
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.c_x = 0
        self.c_y = 0

    def update(self):
        # updates movement
        self.rect.x += self.c_x
        self.rect.y += self.c_y

