import pygame
from .text_lines import YES
from .text_lines import NO
from .text_lines import NOTE_FOUND

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
            self.found()

    def found(self):
        # remove from all_sprites ##i really should make like a sprites
        # manager create, add and remove to from group
        # if next and x is True next += 1 x and false when inside
        self.game.can_move = False
        self.game.decisions = True
        self.game.text_decisions.update_actions("read_note", "back")
        self.game.update_text(self.game.current_text1, NOTE_FOUND)
        self.game.update_text(self.game.decision1, YES)
        self.game.update_text(self.game.decision2, NO)
        self.game.all_sprites.remove(self.game.note)

    def update(self):
        self.collision()
