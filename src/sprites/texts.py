import pygame

class TextBox(pygame.sprite.Sprite):
    """Text bacground box sprite.

    """
    def __init__(self, color, width, height, pos_x, pos_y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update_rect(self,update_y):
        """Box movement.

        Args:
            update_y (int): The y cordinate of the red d_box used for
                indicating which text option is currently being chosen.
        """
        self.rect.y = update_y
