import pygame
from config import RAN_SPEED

class Ran(pygame.sprite.Sprite):
    """Player sprite.

    Attributes:
        game: Game Class
        rect.x: The x cordinate
        rect.y: The y cordinate
        spawn_x: Player's spawn x cordinate.
        spawn_y: Player's spawn y cordinate.
        c_x: Change in x cordinate.
        c_y: Change in y cordinate.
    """
    def __init__(self, game, pos_x, pos_y, image_path):
        super().__init__()

        self.game = game
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.spawn_x = pos_x
        self.spawn_y = pos_y
        self.c_x = 0
        self.c_y = 0

    def spawn(self):
        """Sets the players cordinates to spawn.
        """
        self.rect.x = self.spawn_x
        self.rect.y = self.spawn_y

    def collision(self,axis):
        """Checks for any collisions with the barriers.

        Prevents the player from walking through barriers.

        Args:
            axis (string): The direction which the player is currently moving.

        Attributes:
            collided_wall: A list of all the barriers that the player is colliding with.
        """
        collided_wall = pygame.sprite.spritecollide(self,self.game.barriers, False)
        if axis == "x":
            if len(collided_wall) > 0:
                if self.c_x < 0:
                    self.rect.x = collided_wall[0].rect.right
                if self.c_x > 0:
                    self.rect.x = collided_wall[0].rect.left - self.image.get_width()
                self.c_x = 0
        if axis == "y":
            if len(collided_wall) > 0:
                if self.c_y < 0:
                    self.rect.y = collided_wall[0].rect.bottom
                if self.c_y > 0:
                    self.rect.y = collided_wall[0].rect.top - self.image.get_height()
                self.c_y = 0

    def move(self):
        """Player movement.

        """
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.c_x -= RAN_SPEED
        if pressed_keys[pygame.K_d]:
            self.c_x += RAN_SPEED
        if pressed_keys[pygame.K_s]:
            self.c_y += RAN_SPEED
        if pressed_keys[pygame.K_w]:
            self.c_y -= RAN_SPEED

    def update(self):
        """Updates player movement and checks for any collisions.
        """
        self.move()
        if self.game.can_move is True:
            self.rect.x += self.c_x
            self.collision("x")
            self.rect.y += self.c_y
            self.collision("y")
        self.c_x = 0
        self.c_y = 0
