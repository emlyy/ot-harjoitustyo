import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        