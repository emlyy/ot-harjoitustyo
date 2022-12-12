import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, setter, game, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([50, 90])
        self.game = game
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.where = "second"
        self.setter = setter

    def update_where(self, where):
        self.where = where

    def collision(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            if self.where == "end":
                self.game.running = False
            if self.where == "third":
                self.update_where("end")
                self.setter.third_room(self.game)
            if self.where == "second":
                self.update_where("third")
                self.setter.second_room(self.game)

    def update(self):
        self.collision()
