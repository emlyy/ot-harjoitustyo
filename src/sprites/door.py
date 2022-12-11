import pygame

class Door(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([50, 90])
        self.game = game
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def collision(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.running = False

    def update(self):
        self.collision()
