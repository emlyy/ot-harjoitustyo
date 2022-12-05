import pygame
from .text_lines import YES, NO, NOTE_FOUND

class Note(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, image_path):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def collision(self):
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.text_actions.found(self.game, "read_note", "back", NOTE_FOUND, YES, NO)
            self.game.all_sprites.remove(self.game.note)

    def update(self):
        self.collision()