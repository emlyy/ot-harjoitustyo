import pygame

class TextBox(pygame.sprite.Sprite):
    def __init__(self, color, width, height, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update_rect(self,update_y):
        self.rect.y = update_y
        # when press down cords 3 when up cords 2 ,only used for d_box
