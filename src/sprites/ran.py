import pygame

class Ran(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, image_path):
        super().__init__()

        self.game = game
        self.image = pygame.image.load(image_path)
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.c_x = 0
        self.c_y = 0

    def collision(self,axis):
        collided_wall = pygame.sprite.spritecollide(self,self.game.barriers, False)
        if axis == "x":
            if len(collided_wall) > 0:
                if self.c_x < 0:
                    self.rect.x = collided_wall[0].rect.right
                if self.c_x > 0:
                    self.rect.x = collided_wall[0].rect.left - self.width
                self.c_x = 0
        if axis == "y":
            if len(collided_wall) > 0:
                if self.c_y < 0:
                    self.rect.y = collided_wall[0].rect.bottom
                if self.c_y > 0:
                    self.rect.y = collided_wall[0].rect.top - self.height
                self.c_y = 0

    def update(self):
        self.rect.x += self.c_x
        self.collision("x")
        self.rect.y += self.c_y
        self.collision("y")
