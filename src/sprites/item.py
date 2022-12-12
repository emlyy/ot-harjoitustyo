import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y,
    image_path, decision1, decision2, intro, opt1, opt2):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.game = game
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.decision1 = decision1
        self.decision2 = decision2
        self.intro = intro
        self.opt1 = opt1
        self.opt2 = opt2

    def collision(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.text_actions.found(self.game, self.decision1,
            self.decision2, self.intro, self.opt1, self.opt2)

            self.game.all_sprites.remove(self)

    def update(self):
        self.collision()
