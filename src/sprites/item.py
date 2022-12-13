import pygame

class Item(pygame.sprite.Sprite):
    """Sprite for different items.

    """
    def __init__(self, game, pos_x, pos_y,
    image_path, decision1, decision2, intro, opt1, opt2):
        """
        Args:
            game (Game Class): Connection to game.
            pos_x (int): X cordinate.
            pos_y (int): Y cordinate.
            image_path (str): Path to the image.
            decision1 (str): One of the two decisions that can be made.
            decision2 (str): The other decisions.
            intro (str): Text that will be displayed on top.
            opt1 (str): Text that will be displayed in the middle. Represents
                decision one.
            opt2 (str): Text that will be displayed on the bottom. Represents
                decision two.
        """
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
        """Checks for collisions with the player.
        """
        if pygame.sprite.collide_rect(self, self.game.player):
            self.game.text_actions.found(self.game, self.decision1,
            self.decision2, self.intro, self.opt1, self.opt2)

            self.game.all_sprites.remove(self)

    def update(self):
        self.collision()
