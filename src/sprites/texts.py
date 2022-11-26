import pygame

class TextBox(pygame.sprite.Sprite):
    def __init__(self, game, color, width, height, x, y):
        super().__init__()

        self.game = game

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update_rect(self,y):
        self.rect.y = y       #when press down cords 3 when up cords 2 ,only used for d_box



