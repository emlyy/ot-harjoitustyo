import pygame

class Door(pygame.sprite.Sprite):
    """Door to the next room.

    """
    def __init__(self, setter, game, pos_x, pos_y):
        """
        Args:
            setter (SpriteSet Class): Sets the sprites.
            game (Game Class): Connection to the game.
            pos_x (_type_): X cordinate for door.
            pos_y (_type_): Y cordinate for door.

        Attributes:
            where: A string indicating where the door should lead.
        """
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
        """Checks for collisions with the player.
        """
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
