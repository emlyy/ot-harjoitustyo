import pygame
from .text_lines import ENEMY_NEAR, PUNCH, THROW_ROCK, BOSS, TALK, USE_ITEM

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, image_path, combat_type):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.combat_type = combat_type

    def collision(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            if self.combat_type == "normal":
                self.game.enemies.remove(self)
                self.game.see_enemies.add(self)
                self.game.text_actions.found(self.game, "punch", "throw_rock",
                ENEMY_NEAR, PUNCH, THROW_ROCK)
            else:
                self.game.enemies.empty()
                self.game.text_actions.found(self.game,"talk", "item",BOSS,TALK,USE_ITEM)

    def update(self):
        self.collision()
