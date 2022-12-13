import pygame

class Background(pygame.sprite.Sprite):
    """Displays background images.

    """
    def __init__(self, pos_x, pos_y, image_path):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
